# ----------------[Arquivo_Para_Tirar_Dúvuidas]------------------ #
# Opa! Como estás? :) Esse repositório, como o próprio nome já    #
# diz, tem a função de auxiliar em algumas dúvidas, ou tentar     #
# auxiliar pelo menos. Em uma breve explicação, isso vai ser tipo #
# um wikipedia da vida, onde vai mostrar/relembrar alguns         #
# "tópicos" da linguagem, além de explicar o que seria cada parte.#
#            [Espero que isso ajude de alguma forma!]             #
#           -                  -                     -            #
# ----------------------[Tipos_de_Dados]------------------------- #
# Como primeiro "tópico" temos os 'Tipos de Dados', também chamados
# de Variáveis, essas variáveis tem a função de gardar algum tipo de
# dado, podendo ser eles: carcteres, números inteiros e/ou décimais...
#   +---------------------------------------------------------+   #
#   |   Os Principais Tipos de Dados Padrão do Python São:    |   #
#   +---------------------------------------------------------+   #
#   |  Inteiro                  |           int               |   #
#   |  Ponto Flutuante/Decimal  |          float              |   #
#   |  Lista                    |           List              |   #
#   |  String                   |           str               |   #
#   |  Boolean                  |           bool              |   #
#   |  Tipo Complexo            | [Esqueça por em quanto...]  |   #
#   |  Tuple                    | [Esqueça por em quanto...]  |   #
#   |  Dictionary               | [Esqueça por em quanto...]  |   #
#   +----------------------[Vamos lá!]------------------------+   #
# +-------------------------[Inteiro]---------------------------+ #
# | Tipo 'int', tem como função guarda números Inteiros, ou seja| #
# |números completos. Ex: 1; 2; 3; -21; -777...                 | #
# |--------------------[Exemplo-Em-Código]----------------------| #
idade = int(input("Digite sua idade: "))
print("Você tem", idade, "Anos.")
# +-----------------------[Observações]-------------------------+ #
# | "idade" é o [Nome] da variável, "int" o [Tipo] e o "Input"  | #
# |recebe algum valor (No caso um número), nele também pode ser | #
# |definida algum tipo de mensagem.                             | #
# +-------------------------------------------------------------+ #
# |          -                                       -          | #
# +---------------------[Ponto-Flutuante]-----------------------+ #
# | O 'Ponto flutuante' é um tipo usado para números racionais  | #
# |(números que podem ser representados por uma fração), também | #
# | conhecido como “número quebrado”.                           | #
# +--------------------[Exemplo-Em-Código]----------------------+ #
seu_Salario=float(input("Digite seu salário: "))
print("Você ganha", seu_Salario)
# +-------------------------------------------------------------+ #
# |          -                                       -          | #
# |--------------------------[Listas]---------------------------| #
# | Listas agrupam um conjunto de elementos variados, podendo   | #
# |conter: inteiros, floats, strings, outras listas e outros    | #
# |tipos.                                                       | #
# +--------------------[Exemplo-Em-Código]----------------------+ #
alunos = ['Isac', 'FakeDoIsac', 'Bruno', 'Sarah', 'João']
notas = [9.9, 10, +999, 9.7, 9.9] 
# +-----------------------[Observações]-------------------------+ #
# | Elas são definidas utilizando colchetes para delimitar a    | #
# |lista e vírgulas para separar os elementos.                  | #
# +-------------------------------------------------------------+ #
# |          -                                       -          | #
# |--------------------------[String]---------------------------| #
# | String é uma sequência de caracteres, geralmente utilizada  | #
# |para representar palavras, frases ou textos de um programa.  | #
# |                                                             | #
# +--------------------[Exemplo-Em-Código]----------------------+ #
nome_do_Individuo = input("Digite seu nome: ") 
print("Bem-vindo(a) " + nome_do_Individuo + "!")
# +-------------------------------------------------------------+ #
# |          -                                       -          | #
# |-------------------------[Boolean]---------------------------| #
# | Tipo de dado lógico que pode assumir apenas dois valores:   | #
# |falso ou verdadeiro (False ou True).                         | #
# |                                                             | #
# +--------------------[Exemplo-Em-Código]----------------------+ #
fim_de_semana = True
feriado = False
# +-------------------------------------------------------------+ #
# |      -      01001001 01110011 01100001 01100011      -      | #
# +-------------------------------------------------------------+ #
