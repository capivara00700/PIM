import dbconnect

def exercicios(nome):
    while True:
        print("="*50 + f"\nBem-vindo {nome} ao nosso programa de educação digital!!\nNosso objetivo é criar um ambiente interativo para que você possa \naprender logica de progrmação, boas praticas para proteção de dados \nentre outros assuntos.")
        print("="*50 + "\nPrimeiro escolha o nível que você deseja acessar:")
        print("Nível Fácil [1]\nNível Intermediário [2]")
        escolhaNivel = input("> ")
        print("="*50 + "\nAgora escolha qual tema você deseja acessar: ")
        print("Tipos de Dados [1]\nEstrutura de Controle [2]\nVariáveis e Operadores [3]\nResolução de Problemas [4]")
        escolhaTema = int(input("> "))

        if escolhaNivel == "1":
            quiz(perguntas_faceis, topicos_disponiveis[escolhaTema], "Nível Fácil", nome)
            break
        elif escolhaNivel == "2":
            quiz(perguntas_intermediarias, topicos_disponiveis[escolhaTema], "Nível Intermediário", nome)
            break
        else:
            print("Você selecionou alguma opção inválida, por favor tente novamente.")
#=================================================================================================
def quiz(perguntas, tema, nivel_nome, nome):
    tipos_dados_perguntas = perguntas[tema]

    pontuacao = 0

    print("="*50+f"\nBem vindo ao tópico sobre {tema} ({nivel_nome})\nvocê gostaria de ver uma explicação sobre o assunto [1] \nou ir direto para a nossa atividade interativa? [2]")
    escolha = int(input("> "))

    while True: 
            if escolha == 1:
                print('='*50)
                print(resumos[nivel_nome][tema])
            elif escolha == 2:
                print("="*50+f'\nAqui você podera testar seus conhecimentos sobre \n{tema} e ver como foi o seu desempenho, mas não se preocupe \ncaso erre, você tem varias tentavas. Boa sorte!!!\n')
                for i, pergunta in enumerate(tipos_dados_perguntas, 1):
                    print(f"{i}) {pergunta['pergunta']}")
                    for opcao in pergunta["opcoes"]:
                        print(opcao)
                    resposta = input("> ").lower()
                    
                    if resposta == pergunta["resposta"]:
                        print("✅ Resposta correta!\n")
                        pontuacao += 1
                    else:
                        print(f"❌ Resposta incorreta. {pergunta['explicacao']}\n")
                print(f"🏁 Você acertou {pontuacao} de {len(tipos_dados_perguntas)} perguntas.\n")
                dbconnect.addPontos(pontuacao, nivel_nome, tema, nome) #Adicionando a pontuação
            es = int(input("="*50+'\nOque gostaria de acessar a seguir?\nAtividade [1]\nEscolher outro Nivel/Tema [2]\nFechar o programa [3]\n> '))
            if es == 1:
                escolha == escolha + 1
            elif es == 2:
                exercicios(nome)
            else:
                print('Programa encerrado.')
                break

#=====================================================================================
perguntas_faceis = {
    "Tipos de Dados": [
        {
            "pergunta": "Qual é o tipo de dado do valor 10?",
            "opcoes": ["a) int", "b) str", "c) float", "d) bool"],
            "resposta": "a",
            "explicacao": "O valor 10 é um número inteiro, que em Python é do tipo 'int'."
        },
        {
            "pergunta": "O que significa o tipo 'str'?",
            "opcoes": ["a) número", "b) texto", "c) decimal", "d) verdadeiro/falso"],
            "resposta": "b",
            "explicacao": "'str' significa string, que é o tipo de dado usado para representar textos."
        },
        {
            "pergunta": "Qual destes é um valor booleano?",
            "opcoes": ["a) 100", "b) 'True'", "c) False", "d) 'texto'"],
            "resposta": "c",
            "explicacao": "False é um valor booleano em Python. Valores booleanos são True e False."
        },
        {
            "pergunta": "O valor 3.14 pertence a qual tipo?",
            "opcoes": ["a) int", "b) str", "c) float", "d) bool"],
            "resposta": "c",
            "explicacao": "3.14 é um número decimal, que em Python pertence ao tipo 'float'."
        },
        {
            "pergunta": "O que o tipo bool representa?",
            "opcoes": ["a) texto", "b) número decimal", "c) verdadeiro ou falso", "d) número inteiro"],
            "resposta": "c",
            "explicacao": "O tipo 'bool' representa valores booleanos: True ou False (verdadeiro ou falso)."
        }
    ],
    "Estruturas de Controle": [
        {
            "pergunta": "Qual comando usamos para verificar uma condição?",
            "opcoes": ["a) print", "b) if", "c) input", "d) loop"],
            "resposta": "b",
            "explicacao": "Usamos 'if' para verificar se uma condição é verdadeira e tomar decisões."
        },
        {
            "pergunta": "O que o comando 'else' faz?",
            "opcoes": ["a) repete código", "b) executa se a condição for verdadeira", "c) executa se a condição for falsa", "d) define uma função"],
            "resposta": "c",
            "explicacao": "'else' é executado quando a condição do 'if' é falsa."
        },
        {
            "pergunta": "Qual comando usamos para repetir algo várias vezes?",
            "opcoes": ["a) repeat", "b) if", "c) while", "d) input"],
            "resposta": "c",
            "explicacao": "Usamos 'while' para repetir um bloco de código enquanto a condição for verdadeira."
        },
        {
            "pergunta": "O que significa 'loop infinito'?",
            "opcoes": ["a) erro de sintaxe", "b) repetição que nunca termina", "c) função que retorna True", "d) código que roda uma vez só"],
            "resposta": "b",
            "explicacao": "Um 'loop infinito' é uma repetição que nunca termina, geralmente causada por uma condição que nunca fica falsa."
        },
        {
            "pergunta": "O que 'if x > 10:' verifica?",
            "opcoes": ["a) se x é igual a 10", "b) se x é menor que 10", "c) se x é maior que 10", "d) se x é diferente de 10"],
            "resposta": "c",
            "explicacao": "A expressão 'x > 10' verifica se x é maior que 10."
        }
    ],
    "Variáveis e Operadores": [
        {
            "pergunta": "Qual símbolo usamos para somar em Python?",
            "opcoes": ["a) -", "b) +", "c) *", "d) /"],
            "resposta": "b",
            "explicacao": "O símbolo '+' é usado para somar dois números em Python."
        },
        {
            "pergunta": "Qual operador usamos para subtração?",
            "opcoes": ["a) +", "b) *", "c) -", "d) /"],
            "resposta": "c",
            "explicacao": "O operador '-' realiza a subtração de valores."
        },
        {
            "pergunta": "Como criamos uma variável chamada idade?",
            "opcoes": ["a) idade = 20", "b) 20 = idade", "c) idade == 20", "d) var idade = 20"],
            "resposta": "a",
            "explicacao": "A atribuição correta em Python é: nome = valor. Ex: idade = 20."
        },
        {
            "pergunta": "O que faz o operador '*'?",
            "opcoes": ["a) soma", "b) divisão", "c) multiplicação", "d) subtração"],
            "resposta": "c",
            "explicacao": "O operador '*' multiplica dois números em Python."
        },
        {
            "pergunta": "Como chamamos um nome usado para armazenar um valor?",
            "opcoes": ["a) função", "b) operador", "c) variável", "d) laço"],
            "resposta": "c",
            "explicacao": "Uma variável é um nome que usamos para guardar um valor na memória."
        }
    ],
    "Resolução de Problemas": [
        {
            "pergunta": "O que é o primeiro passo para resolver um problema com programação?",
            "opcoes": ["a) copiar código", "b) entender o problema", "c) escrever qualquer coisa", "d) pular etapas"],
            "resposta": "b",
            "explicacao": "Antes de escrever código, é fundamental entender o problema que você quer resolver."
        },
        {
            "pergunta": "Por que é importante planejar antes de programar?",
            "opcoes": ["a) para gastar tempo", "b) para evitar erros", "c) para copiar melhor", "d) para decorar comandos"],
            "resposta": "b",
            "explicacao": "Planejar ajuda a evitar erros e a escrever um código mais eficiente."
        },
        {
            "pergunta": "O que podemos usar para pensar nos passos do programa?",
            "opcoes": ["a) um mapa", "b) receita de bolo", "c) algoritmo", "d) livro"],
            "resposta": "c",
            "explicacao": "Um algoritmo é uma sequência de passos para resolver um problema."
        },
        {
            "pergunta": "Qual é uma boa prática ao testar um programa?",
            "opcoes": ["a) testar só uma vez", "b) não testar", "c) testar com exemplos diferentes", "d) apagar o código"],
            "resposta": "c",
            "explicacao": "Testar com exemplos diferentes ajuda a garantir que o programa funciona em vários casos."
        },
        {
            "pergunta": "Se o código deu erro, o que devemos fazer?",
            "opcoes": ["a) apagar tudo", "b) ler o erro e tentar corrigir", "c) ignorar", "d) fechar o programa"],
            "resposta": "b",
            "explicacao": "Ler a mensagem de erro pode ajudar a encontrar e corrigir o problema."
        }
    ]
}


perguntas_intermediarias = {
    "Tipos de Dados": [
        {
            "pergunta": "Qual é o tipo do valor 3.14 em Python?",
            "opcoes": ["a) int", "b) str", "c) float", "d) bool"],
            "resposta": "c",
            "explicacao": "3.14 é um número decimal, representado pelo tipo float em Python."
        },
        {
            "pergunta": "Qual é o tipo de dado do valor 'True' (sem aspas)?",
            "opcoes": ["a) int", "b) str", "c) bool", "d) float"],
            "resposta": "c",
            "explicacao": "'True' em Python (sem aspas) é um valor booleano, que representa verdadeiro."
        },
        {
            "pergunta": "O que acontece se somarmos uma string e um número?",
            "opcoes": ["a) Soma os valores", "b) Concatena", "c) Dá erro", "d) Multiplica"],
            "resposta": "c",
            "explicacao": "Em Python, não podemos somar string com número diretamente; isso gera um erro."
        },
        {
            "pergunta": "Qual é o tipo da variável resultado = '5' + '10'?",
            "opcoes": ["a) int", "b) float", "c) str", "d) bool"],
            "resposta": "c",
            "explicacao": "A soma de duas strings com '+' resulta em outra string: '510'."
        },
        {
            "pergunta": "O que a função type() retorna?",
            "opcoes": ["a) O valor da variável", "b) O nome da variável", "c) O tipo do dado", "d) O endereço de memória"],
            "resposta": "c",
            "explicacao": "A função type() mostra qual é o tipo de dado de um valor ou variável."
        }
    ],
    "Estruturas de Controle": [
        {
            "pergunta": "Qual dessas estruturas permite repetir um bloco até que uma condição seja falsa?",
            "opcoes": ["a) if", "b) else", "c) while", "d) break"],
            "resposta": "c",
            "explicacao": "'while' repete o bloco enquanto a condição for verdadeira, e para quando ela for falsa."
        },
        {
            "pergunta": "Em qual estrutura usamos o 'elif'?",
            "opcoes": ["a) if", "b) while", "c) for", "d) try"],
            "resposta": "a",
            "explicacao": "'elif' é usado junto com 'if' para testar outra condição caso a primeira seja falsa."
        },
        {
            "pergunta": "Qual será a saída de: if 10 > 5: print('A') else: print('B')?",
            "opcoes": ["a) A", "b) B", "c) AB", "d) Erro"],
            "resposta": "a",
            "explicacao": "10 é maior que 5, então a condição é verdadeira e 'A' será exibido."
        },
        {
            "pergunta": "Qual palavra-chave usamos para sair de um laço?",
            "opcoes": ["a) stop", "b) exit", "c) end", "d) break"],
            "resposta": "d",
            "explicacao": "'break' é usado para interromper um laço antes que ele termine normalmente."
        },
        {
            "pergunta": "O que acontece se a condição de um while nunca for falsa?",
            "opcoes": ["a) O programa termina", "b) O laço não inicia", "c) Ocorre um erro", "d) Entra em loop infinito"],
            "resposta": "d",
            "explicacao": "Se a condição nunca for falsa, o laço 'while' repetirá para sempre — isso é um loop infinito."
        }
    ],
    "Variáveis e Operadores": [
        {
            "pergunta": "Qual é o valor de x após: x = 10; x = x + 5?",
            "opcoes": ["a) 5", "b) 10", "c) 15", "d) 20"],
            "resposta": "c",
            "explicacao": "x começa com 10 e depois soma 5, então o novo valor de x é 15."
        },
        {
            "pergunta": "Qual operador usamos para comparar igualdade?",
            "opcoes": ["a) =", "b) !=", "c) ==", "d) =="],
            "resposta": "d",
            "explicacao": "'==' é usado para comparar se dois valores são iguais. '=' é usado para atribuição."
        },
        {
            "pergunta": "O que x = x * 2 faz?",
            "opcoes": ["a) Dobra o valor de x", "b) Divide x", "c) Soma 2 a x", "d) Apaga x"],
            "resposta": "a",
            "explicacao": "O valor de x será multiplicado por 2 e atualizado."
        },
        {
            "pergunta": "Qual o resultado de 10 // 3?",
            "opcoes": ["a) 3.33", "b) 3", "c) 4", "d) 1"],
            "resposta": "b",
            "explicacao": "'//' faz divisão inteira, ou seja, sem o valor decimal. 10 dividido por 3 dá 3 inteiro."
        },
        {
            "pergunta": "Qual operador retorna o resto da divisão?",
            "opcoes": ["a) /", "b) //", "c) %", "d) **"],
            "resposta": "c",
            "explicacao": "'%' retorna o resto de uma divisão. Ex: 10 % 3 = 1."
        }
    ],
    "Resolução de Problemas": [
        {
            "pergunta": "Qual é a melhor maneira de entender um problema antes de programar?",
            "opcoes": ["a) Ignorar o enunciado", "b) Fazer testes", "c) Ler com atenção e identificar as entradas e saídas", "d) Escrever o código direto"],
            "resposta": "c",
            "explicacao": "Entender o que entra e o que deve sair ajuda a estruturar a lógica corretamente."
        },
        {
            "pergunta": "Para resolver um problema com código, o que devemos fazer primeiro?",
            "opcoes": ["a) Programar", "b) Testar", "c) Planejar os passos", "d) Copiar código da internet"],
            "resposta": "c",
            "explicacao": "Planejar os passos ajuda a organizar as ideias e resolver o problema com lógica."
        },
        {
            "pergunta": "Qual dessas ferramentas ajuda a representar visualmente a lógica de um algoritmo?",
            "opcoes": ["a) Gráfico de barras", "b) Fluxograma", "c) Lista", "d) Tabela verdade"],
            "resposta": "b",
            "explicacao": "Fluxogramas mostram o fluxo de decisões e ações em um algoritmo de forma visual."
        },
        {
            "pergunta": "Se o código não está funcionando, qual a melhor atitude?",
            "opcoes": ["a) Apagar tudo", "b) Testar partes menores", "c) Desistir", "d) Ignorar os erros"],
            "resposta": "b",
            "explicacao": "Testar partes menores ajuda a identificar onde está o erro na lógica ou sintaxe."
        },
        {
            "pergunta": "Por que é importante testar diferentes cenários no código?",
            "opcoes": ["a) Para gastar tempo", "b) Para dificultar", "c) Para garantir que funcione em várias situações", "d) Para ver a tela piscar"],
            "resposta": "c",
            "explicacao": "Testar diferentes casos ajuda a garantir que o código está correto em todas as situações."
        }
    ]
}
resumos = {
        "Nível Fácil": {
            "Tipos de Dados": ("""
Em programação, tipos de dados indicam o tipo de informação com que estamos lidando.
Os principais são:
- int (inteiro): números como 5, -3, 100.
- float (decimal): números com ponto, como 3.14.
- str (string): textos entre aspas, como "olá".
- bool (booleano): verdadeiro (True) ou falso (False).

Cada tipo tem comportamentos diferentes e é usado para diferentes tarefas.
"""
            ),
            "Estruturas de Controle": ( """
As estruturas de controle determinam o fluxo do programa. Por exemplo:
- if: executa algo se uma condição for verdadeira.
- else: executa algo se a condição for falsa.
- while: repete uma ação enquanto uma condição for verdadeira.

Elas permitem que o programa tome decisões e repita comandos quando necessário.
"""
            ),
            "Variáveis e Operadores": ( """
Uma variável é como uma caixinha com um nome, onde guardamos um valor.
Exemplo: idade = 20

Operadores são símbolos que fazem operações:
- + soma
- - subtração
- * multiplicação
- / divisão

Juntos, variáveis e operadores nos permitem guardar e calcular valores.
"""
            ),
            "Resolução de Problemas": ( """
Resolver problemas em programação envolve:
1. Entender o problema.
2. Pensar nos passos para resolvê-lo.
3. Escrever esses passos no código.
4. Testar e corrigir se necessário.

Dividir o problema em partes menores ajuda muito!
"""
        )
        },
        "Nível Intermediário": {
            "Tipos de Dados": ( """
Além de saber quais são os tipos (int, float, str, bool), é importante entender como eles interagem:
- "5" + "3" = "53" (texto concatenado)
- 5 + 3 = 8 (soma numérica)

Você também pode converter entre tipos:
- int("10") → 10
- str(50) → "50"

Saber converter tipos evita erros e dá mais controle sobre o que o programa faz.
"""
            ),
            "Estruturas de Controle": ( """
Comandos como if, elif, else, for e while ajudam o programa a tomar decisões e repetir ações:
- if...elif...else: avaliam várias possibilidades.
- for: repete algo um número certo de vezes.
- while: repete enquanto a condição for verdadeira.

Exemplo:
for i in range(5):
    print(i)
Isso imprime os números de 0 a 4.
"""
            ),
            "Variáveis e Operadores": ( """
Além dos operadores básicos (+, -, *, /), usamos comparações:
- == igual
- != diferente
- > maior
- < menor
- >= maior ou igual
- <= menor ou igual

E operadores lógicos:
- and: verdadeiro se duas condições forem verdadeiras.
- or: verdadeiro se pelo menos uma for.
- not: inverte o valor lógico.

Esses recursos tornam as decisões do programa mais inteligentes.
"""
            ),
            "Resolução de Problemas": ( """
Resolver problemas envolve pensar na lógica antes de programar:
1. Entrada: o que o usuário fornece.
2. Processamento: o que o programa faz com isso.
3. Saída: o que será mostrado ao final.

Planejar bem usando algoritmos (passo a passo) ajuda muito.
Um bom planejamento evita erros e economiza tempo.
"""
            )
        }
    }
topicos_disponiveis = {
    1: "Tipos de Dados",
    2: "Estruturas de Controle",
    3: "Variáveis e Operadores",
    4: "Resolução de Problemas"
}
