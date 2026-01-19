from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime
import os

app = Flask(__name__)

def resultados_gerados_csv(vencedor_do_quiz):
    arquivo_resultados_gerados = "resultados_gerados.csv"
    
    agora = datetime.now()
    data_do_resultado = agora.strftime("%d/%m/%Y %H:%M")
    existe_arquivo = os.path.exists(arquivo_resultados_gerados)

    try:
        with open(arquivo_resultados_gerados, "a", encoding="utf-8", newline='') as h:
            escrever = csv.writer(h)
    
            if existe_arquivo == False:
                cabecalho = ["Data e hora", "Personagem vencedor"]
                escrever.writerow(cabecalho)

            linha_para_salvar = [data_do_resultado, vencedor_do_quiz]
            escrever.writerow(linha_para_salvar)

    except Exception as erro:
        print(f"Erro ao salvar: {erro}")

def ler_perguntas_do_arquivo():
    perguntas_estruturadas = []
    
    try:
        arquivo = open("perguntas.txt", 'r', encoding="utf-8")
        linhas = arquivo.readlines()
        arquivo.close()
    except FileNotFoundError:
        return []

    pergunta_atual = None
    numero_pergunta = 0

    for linha in linhas:
        linha = linha.strip()
        
        if linha == "":
            continue

        primeiro_caractere = linha[0]
        if primeiro_caractere.isdigit() and ")" in linha:
            numero_pergunta = numero_pergunta + 1
            
            pergunta_atual = {}
            pergunta_atual["numero"] = numero_pergunta
            pergunta_atual["titulo"] = linha
            pergunta_atual["alternativas"] = []
            
            perguntas_estruturadas.append(pergunta_atual)


        elif "|" in linha:
            partes = linha.split('|')
            
            if len(partes) > 1:
                texto_da_alternativa = partes[0].strip()
                nome_personagem = partes[1].strip()
                dados_alternativa = {}
                dados_alternativa["texto"] = texto_da_alternativa
                dados_alternativa["personagem"] = nome_personagem
                pergunta_atual["alternativas"].append(dados_alternativa)
    
    return perguntas_estruturadas

def ler_desempate(personagens_empatados):
    try:
        arquivo = open("pergunta_desempate.txt", "r", encoding="utf-8")
        linhas = arquivo.readlines()
        arquivo.close()
    except FileNotFoundError:
        return None

    titulo = linhas[0].strip()
    
    opcoes_validas = []
    letras_disponiveis = "abcdefgh"
    contador = 0

    for linha in linhas:
        if "|" in linha:
            partes = linha.split('|')
            personagem = partes[1].strip()
            texto_bruto = partes[0].strip()
            esta_no_empate = False
            for p in personagens_empatados:
                if p == personagem:
                    esta_no_empate = True
            
            if esta_no_empate == True:
                if ") " in texto_bruto:
                    texto_limpo = texto_bruto.split(") ")[1]
                else:
                    texto_limpo = texto_bruto
            
                nova_letra = letras_disponiveis[contador]
                
                nova_opcao = {}
                nova_opcao["texto"] = f"{nova_letra}) {texto_limpo}"
                nova_opcao["personagem"] = personagem
                
                opcoes_validas.append(nova_opcao)
                contador = contador + 1
    
    resultado_final = {}
    resultado_final["titulo"] = titulo
    resultado_final["opcoes"] = opcoes_validas
    
    return resultado_final


@app.route('/')
def index():
    lista_perguntas = ler_perguntas_do_arquivo()
    return render_template('index.html', perguntas=lista_perguntas)

@app.route('/calcular', methods=['POST'])
def calcular():
    respostas = request.form
    pontuacoes = {}
    pontuacoes['Rosalie'] = 0
    pontuacoes['Edward'] = 0
    pontuacoes['Alice'] = 0
    pontuacoes['Charlie'] = 0
    pontuacoes['Emmett'] = 0
    pontuacoes['Jacob'] = 0
    pontuacoes['Jasper'] = 0
    pontuacoes['Bella'] = 0

    for campo in respostas:
        personagem_escolhido = respostas[campo]
        
        if personagem_escolhido in pontuacoes:
            if campo == 'pergunta_9':
                pontuacoes[personagem_escolhido] = pontuacoes[personagem_escolhido] + 3
            else:
                pontuacoes[personagem_escolhido] = pontuacoes[personagem_escolhido] + 1

    maior_pontuacao = 0
    for nome in pontuacoes:
        pontos = pontuacoes[nome]
        if pontos > maior_pontuacao:
            maior_pontuacao = pontos
    empatados = []
    for nome in pontuacoes:
        pontos = pontuacoes[nome]
        if pontos == maior_pontuacao:
            empatados.append(nome)

    quantidade_empatados = len(empatados)

    if quantidade_empatados > 1:
        dados_desempate = ler_desempate(empatados)
        string_empatados = ",".join(empatados)
        
        return render_template('desempate.html', 
                             pergunta=dados_desempate, 
                             empatados_str=string_empatados)
    else:
        vencedor = empatados[0]
        resultados_gerados_csv(vencedor)
        return render_template('resultado.html', vencedor=vencedor)

@app.route('/finalizar_desempate', methods=['POST'])
def finalizar_desempate():
    vencedor = request.form.get('vencedor_final')
    resultados_gerados_csv(vencedor)
    return render_template('resultado.html', vencedor=vencedor)

if __name__ == '__main__':
    app.run(debug=True)
