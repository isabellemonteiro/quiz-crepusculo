import csv
from datetime import datetime
import os

def resultados_gerados_csv(vencedor_do_quiz):
    arquivo_resultados_gerados = "resultados_gerados.csv"

    data_do_resultado = datetime.now().strftime("%d/%m/%Y %H:%M")
    arquivo = os.path.exists(arquivo_resultados_gerados)

    try:
        with open(arquivo_resultados_gerados, "a", encoding="utf-8") as h:
            escrever = csv.writer(h)
            
            if not arquivo:
                
                escrever.writerow(["Data e hora", "Personagem vencedor"])

            escrever.writerow([data_do_resultado, vencedor_do_quiz])
                
        print(f"\nResultado salvo em {arquivo_resultados_gerados}!")

    except Exception as erros_causados:
        print(f"\nOcorreu um erro: {erros_causados}")
    except FileNotFoundError:
        print(f"Arquivo {arquivo_resultados_gerados} não encontrado")
    except PermissionError:
        print("Ocorreu um erro na permissão para escrever no arquivo.")
    except csv.Error as erros_causados:
        print(f"Erro no csv: {erros_causados}")

def rodar_quiz(arquivo_das_perguntas):

    pontuacoes = {
        'Rosalie': 0, 'Edward': 0, 'Alice': 0, 'Charlie': 0,
        'Emmett': 0, 'Jacob': 0, 'Jasper': 0, 'Bella': 0
    }
    
    pergunta_atual = 0

    

    try:
        with open(arquivo_das_perguntas, 'r', encoding="utf-8") as f:
            linhas = f.readlines()
    except FileNotFoundError:
        print(f"O {arquivo_das_perguntas} não encontrado.")
        return


    for linha in linhas:
        linha = linha.strip()
        if not linha: continue
        
        

        if linha[0].isdigit() and ")" in linha[:4]:
            pergunta_atual += 1
            print(linha)


            personagens_do_quiz = {}

        elif ")" in linha[:3]:
            partes = linha.split('|')
            if len(partes) > 1:
                letra = linha[0].lower()
                texto_das_alternativa = partes[0].strip()
                nome_personagem = partes[1].strip()
                
                personagens_do_quiz[letra] = nome_personagem
                print(texto_das_alternativa)


            if linha.lower().startswith('h)'):
                while True:
                    letras_validas = "abcdefghABCDEFGH"
                    escolha = input("\n Sua resposta: ").lower().strip()

                    if escolha not in letras_validas or escolha == "":
                        print("Opção inválida!")
                    else:
                        resposta_usuario = personagens_do_quiz[escolha]
                        
                        pontos = 0

                        if pergunta_atual == 9:
                            pontos += 3
                            
                        pontuacoes[resposta_usuario] += 1
                        break



    maior_pontuacao = max(pontuacoes.values())
    personagens_empatados = [personagem for personagem, pontos in pontuacoes.items() if pontos == maior_pontuacao]

    if len(personagens_empatados) > 1:
        print("Pergunta extra!")
       

        try:
            with open("pergunta_desempate.txt", "r", encoding="utf-8") as g:
                pergunta_do_desempate = g.readlines()
            
            print(f"\nHouve um empate entre: {', '.join(personagens_empatados)}")
            print(f"\n{pergunta_do_desempate[0].strip()}") 
            
            opcoes_finais = {}
            cont_letra = 0
            
            for i in pergunta_do_desempate:
                if "|" in i:
                    partes_da_pergunta = i.split("|")
                    nome_dos_persoangens_empate = partes_da_pergunta[1].strip()
                    
                    if nome_dos_persoangens_empate in personagens_empatados:
                        letra_da_pergunta_desempate = chr(97 + cont_letra)

                        opcoes_finais[letra_da_pergunta_desempate] = nome_dos_persoangens_empate

                        texto_pergunta_desempate = partes_da_pergunta[0].strip().split(") ")[1]

                        print(f"{letra_da_pergunta_desempate}) {texto_pergunta_desempate}")
                        cont_letra += 1

            while True:
                decisao = input("\nSua escolha final: ").lower().strip()
                if decisao in opcoes_finais:
                    vencedor_do_empate = opcoes_finais[decisao]
                    pontuacoes[vencedor_do_empate] += 5
                    break

        except FileNotFoundError:
            print("Erro: O arquivo da pergunta do desempate não foi encontrado.")
            vencedor_do_empate = personagens_empatados[0]
    else:
        vencedor_do_empate = personagens_empatados[0]

    resultados_gerados_csv(vencedor_do_empate)

    print("\n" + "_"*40)
    print("\nResultado final")
    print("_"*40)
    
    print(f"\nSeu namorado em Crepúsculo seria: {vencedor_do_empate.upper()}!")


rodar_quiz("perguntas.txt")