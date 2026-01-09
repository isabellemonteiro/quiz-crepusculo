O nosso projeto é um quiz, com tema Crepúsculo onde é um teste de compatibilidade para saber quem seria seu namorado em Crepusculo, nele há 8 opções de personagens.

Essa parte do código mostra as bibliotecas que foram utilizadas.
        import csv
        from datetime import datetime
        import os


Essa parte do código ela inicializa uma funaçao, que tem o objetivo de salvar os resultados e salvar no arquivo resultados_gerados.csv
        def resultados_gerados_csv(vencedor_do_quiz):


Essa parte do código cria uma variavel com o nome do arquivo que será editado
        arquivo_resultados_gerados = "resultados_gerados.csv"


Essa parte do código exibe a data completa. O datetime.now() pega a data exata e o .strtime("%d/%m/%Y") fortama essa data colocando o dia/mês/ano
        data_do_resultado = datetime.now().strftime("%d/%m/%Y %H:%M")


Essa parte do código verifica se o arquivo ja existe. Utilizamos a blioteca "os" e o .path.exist() , que é uma função que verifica se o arquivo ja existe na pasta do projeto
        arquivo = os.path.exists(arquivo_resultados_gerados)


Essa parte do código utilizamos o try e dentro dele usamos o with para abrir o arquivo que sera colocado os resultados gerados.
        try:
                with open(arquivo_resultados_gerados, "a", encoding="utf-8") as h:


Essa parte do código transforma o arquivo aberto que foi chamado de h para o formato de planilhas.
        escrever = csv.writer(h)


Essa parte do código com o comando writerow() escreve uma linha inteira, depois é expresso a data e o personagem vencedor.
         if not arquivo:
                
                escrever.writerow(["Data e hora", "Personagem vencedor"])
            escrever.writerow([data_do_resultado, vencedor_do_quiz])


Essa parte do código exibe para o usuário em que arquivo o seu resultado foi guardado.
        print(f"\nResultado salvo em {arquivo_resultados_gerados}!")


Essa parte do código é o except, que aparece caso haja um erro no try. O Exception detecta os erros e depois esses erros são guardados e depois serão exibidos.
        except Exception as erros_causados:
                print(f"\nOcorreu um erro: {erros_causados}")



Essa parte do código ela começa a pontuaçao antes das perguntas serem exibidas, associando um valor neutro, que quando o usuário responder, um valor será atribuido:
        pontuacoes = {
                'Rosalie': 0, 'Edward': 0, 'Alice': 0, 'Charlie': 0,
                'Emmett': 0, 'Jacob': 0, 'Jasper': 0, 'Bella': 0
        } 


Essa parte inicializa um contador simples, para que posteriormente, em um laço de repetiçao seja exibida as perguntas:
        pergunta_atual = 0


Essa parte do código tenta abir e se caso o arquivo não seja encontrado, é mostrado uma mensagem. Com o with, ele abre e fecha automaticamente.
        try:
                with open(arquivo_das_perguntas, 'r', encoding="utf-8") as f:
                    linhas = f.readlines()
        except FileNotFoundError:
                print(f"O {arquivo_das_perguntas} não encontrado.")
                return



Essa parte percorre todas as linhas que tiverem no arquivo de texto. O strip vai limpar o arquivo e o if not linha: continue evita que ocorra problemas caso haja espaços em branco

        for linha in linhas.
        linha = linha.strip()
        if not linha: continue

Essa parte do código identifica a pergunta em si.
        if linha[0].isdigit() and ")" in linha[:4]:
            pergunta_atual += 1
            print(linha)

            personagens_do_quiz = {}

O linha[0] identifica o primeiro caractere da linha que está sendo processada. o isdigit() identifica se esse primeiro caractere é um número e o and ")" e in linha[:4] significa que a ao ler a linha se tiver o primeiro caractere um número acompanhado de ")" ate os quatro primeiros caracteres ela vai cumprir esses requisitos.

O pergunta_atual += 1 simboliza que se a linha cumprir esses requisitos, vai ser detectado essa pergunta e somado +1, depois é mostrado essa linha.


Essa parte inicia um dicionário vazio, guardando o nome de cada personagem correspondente das alternativas. Sem essa parte, o código não sabaria onde colocar os pontos.
            personagens_do_quiz = {}


Essa parte do código verifica se até os 3 primeiros caracteres tiverem ")" ele vai cumprir algumas exigencias
                elif ")" in linha[:3]:


Essa parte do código vai separar toda a frase quando ver "|"
                    partes = linha.split('|')

Ex: a) Estar ao lado de alguém que me ajude a recuperar o que sinto que me foi roubado na vida. | Rosalie

Como o computador vai entender:

'Estar ao lado de alguém que me ajude a recuperar o que sinto que me foi roubado na vida. ', ' Rosalie'




Essa parte do código vai medir o tamanho da lista que foi criada pelo split, continuando só se estiver alguma coisa depois da barra.
        if len(partes) > 1:


Essa parte do código pega o primeiro caractere e a transforma automaticamente em minúscula
        letra = linha[0].lower()


Essa parte do código pega a parte que esta antes da barra e com o strip ele vai limpar a frase, tirando os espaços antes e depois da frase.
        texto_das_alternativa = partes[0].strip()


Essa parte do código pega tudo que vier depois da barra, o nome do personagem correspondente a cada alternativa, com o strip vai ocorrer a limpeza dos espaços que estão no inicio
        nome_personagem = partes[1].strip().replace("-", "").strip()


Essa parte do código vai associar a letra com o determinado personagem e depois vai exibir o texto das alternativas.
        personagens_do_quiz[letra] = nome_personagem
        print(texto_das_alternativa)


Essa parte do código seleciona a linha, transforma-a inteiramente em minúscula e verifica se começa com a letra h, ou seja, vai ser selecionado apenas a ultima alternativa.
        if linha.lower().startswith('h)'):


Essa parte do código é o while e está determinando as letras que podem ser digitadas e com a solicitação da alternativa escolhida, o que o usuáriodigitar vai ser transformado em minúsculo e retirado os espaços devido ao uso do strip.
        while True:
            letras_validas = "abcdefghABCDEFGH"
            escolha = input("\n Sua resposta: ").lower().strip()


Essa parte do código faz um tratamento de erro,caso o usuário digite letras que não estão detras das letras validas ou não digite nada vai aparecer uma mensagem que a opção está inválida. Então como esse if está dentro de um while, enquanto o usuario não digitar uma letra válida essa mensagem ainda aparecerá.
        if escolha not in letras_validas or escolha == "":
            print("Opção inválida!")    


Essa parte do código vai associar o pesonagem da alternativa escolhida com a alternativa.
        else:
            voto = personagens_do_quiz[escolha]


Essa parte do código cria uma variavel dos pontos, e que se a pergunta for a 9, a pontuaçao vai ser maior que as demais alternativas e depois o break para esse while.
        pontos = 0

        if pergunta_atual == 9:
            pontos += 2

                        
        pontuacoes[voto] += 1
            break


Essa parte do código encontra o maior numero apenas os pontos que estao dentro do dicionario pontuações. Essa linha do código analisa a maior pontuação atingida.
        maior_pontuacao = max(pontuacoes.values())


Essa parte do código extrai o nome e os pontos e verifica quais personagens ficaram com a pontuação maxima e cria uma lista desses persoangens que estão com as pontuações empatadas.
        personagens_empatados = [personagem for personagem, pontos in pontuacoes.items() if pontos == maior_pontuacao]


Essa parte do código certifica se há mais de 1 personagem com a maior pontuação, e caso tiver, verifica quantos personagens estão empatados e em seguida é exibido ao usuario que terá uma pergunta extra.
        if len(personagens_empatados) > 1:
            print("Pergunta extra!")


Essa parte do código é iniado um try e um except, no try é soliciado a abertura do arquivo que está a pergunta extra caso não seja possivel abrir o arquivo, o usuario recebe uma mensagem que o aquivo não pode ser aberto.
         try:
            with open("pergunta_desempate.txt", "r", encoding="utf-8") as g:
                pergunta_do_desempate = g.readlines()
        
        except FileNotFoundError:
                print("Erro: O arquivo da pergunta do desempate não foi encontrado.")


Essa parte do código abre o arquivo "pergunta_desempate.txt" e é chamado de g.
        with open("pergunta_desempate.txt", "r", encoding="utf-8") as g:


Essa parte do código lê todas as linhas do arquivo e as guarda na lista pergunta_do_desempate.
        pergunta_do_desempate = g.readlines()


Essa parte do código seleciona os nomes dos persoangens empatados e os separa com ", ". O .join junta todos os nomes com a separaçao indicada.
        print(f"\nHouve um empate entre: {', '.join(personagens_empatados)}")


Essa parte do código extrai a linha da posição 0, ou seja, o enunciado da questão extra que foi lida e adicionada todas as linhas na lista pergunta_do_desempate.
        print(f"\n{pergunta_do_desempate[0].strip()}") 



Essa parte do código criou um dicionario e um contador para criar as letras das opções dos personagens empatados.
        opcoes_finais = {}
        cont_letra = 0


Essa parte do código percorre cada linha da lista pergunta_do_desempate, depois no if, se tiver na linha que esta sendo percorrida um "|", vai ser separado a partir do split a linha, separando a linha na resposta e o personagem correspondente a alternativa.
        for i in pergunta_do_desempate:
            if "|" in i:
            partes_da_pergunta = i.split("|")


Essa parte do código extrai o nome do personagem daquela alternativa,que foi separada da frase anteriormente pelo split, e é limpa os espaços a partir do strip.
        nome_dos_persoangens_empate = partes_da_pergunta[1].strip()


Essa parte do código verifica se o nome do personagem está na lista dos personagens empatados.
        if nome_dos_persoangens_empate in personagens_empatados:


Essa parte do código utiliza o chr() que transforma numeros em letras. O número 97 de acordo com a tabela computacional representa a letra "a". Com isso, quando o contador for 0, a letra que será exibida para o usuario será "a", quando for 1 será "b".
        letra_atual = chr(97 + cont_letra)


Essa parte do código guarda no dicionario que a letra vai ser correspondente a um dos persoangens que estão empatados.
        opcoes_finais[letra_atual] = nome_dos_persoangens_empate


Essa parte do código seleciona a primeira parte do código, o texto das alternativas, é limpa com o strip, e separa o ") " que há deixando realmente só a resposta.
        exto_pergunta_desempate = partes_da_pergunta[0].strip().split(') ')[1]


Essa parte do código exibe a pergunta com a letra + ) + o texto.
        print(f"{letra_da_pergunta_desempate} {texto_pergunta_desempate}")


Essa parte do código adiciona um novo valor para que com o proximo personagem a letra esteja em sequência alfabetíca.
        cont_letra += 1


Essa parte do código cria um laço de repetiçao para o usuario digitar a resposta. A variavel decisao com a resposta do usuario tranforma a resposta em minúscula e é limpa usando o strip.
        while True:
                decisao = input("\nSua escolha final: ").lower().strip()



Essa parte do código verifica se a opção escolhida pelo usuario está dentro do dicionario opcoes_finais.
        if decisao in opcoes_finais:


Essa parte do código atribui o vencedor a partir da opçao que o usuario digitou e depois atrbui uma pontuaçao à aquele escolhido pelo usuario. Deopis o while é encerrado.
         vencedor_do_empate = opcoes_finais[decisao]
         pontuacoes[vencedor_do_empate] += 5
            break


Essa parte do código aparece caso não seja encontrado ou não exista o arquivo pergunta_desempate.txt. E caso haja um empate e não é possivel abrir o arquivo, vai ser exibido que o vencedor será o primeiro nome da lista.
         except FileNotFoundError:
            print("Erro: O arquivo da pergunta do desempate não foi encontrado.")
            vencedor_do_empate = personagens_empatados[0]


Essa parte do código é o else de [if len(personagens_empatados) > 1: print("Pergunta extra!")] essa parte só é executada quando não há empate, ou seja como só há um personagem com nota maxima, ele será o vencedor.
        else:
            vencedor_do_empate = personagens_empatados[0]


Essa parte do código possibilita que a funçao resultados_gerados_csv realmente funcione e salve os resultados.
        resultados_gerados_csv(vencedor_do_empate)

        
Essa parte do código exibe o resultado final de quem seria o seu namorado em Crepúsculo.
                print("\n" + "_"*40)
                print("\nResultado final")
                print("_"*40)
    
                print(f"\nSeu namorado em Crepúsculo seria: {vencedor_do_empate.upper()}!")




Participantes: Mariana Sophia, Mariluz Pereira, Aimée Debora e Isabelle Nóbrega