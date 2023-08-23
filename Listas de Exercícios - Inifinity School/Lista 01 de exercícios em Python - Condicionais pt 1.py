# Faça um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem informando que ele foi multado. Além disso, calcule o valor da multa que irá custar R$70,00 por cada km passado acima do limite.
limite_de_velocidade = 80
velocidade_registrada = int(input('Insira a velocidade registrada pelo radar'))
valor_da_multa=float(velocidade_registrada - limite_de_velocidade)*70.00
if velocidade_registrada > limite_de_velocidade:
    print(f'Você excedeu o limite de velocidade de 80km/h, deverá efetuar o pagamento de uma multa no valor de R${valor_da_multa}')
else:
    print('Você não excedeu o limite de velocidade')
    
## Faça um programa que leia num número inteiro e mostre na tela se ele é par ou ímpar
n1 = int(input('Digite um número'))
if n1 % 2 == 0:
    print('Esse número é par')
else: print('Esse número é ímpar')

"""Faça um programa que pergunte a distância de uma viagem em quilômetros. Calcule o preço da passagem do ônibus, cobrando R$ 0,85 por cada km rodado para viagens de até 200 km e R$ 0,57 para viagens com mais de 200 km
INPUT: Total de km = 250
>>> O preço da passagem é R$ 142,50
INPUT: n = 175
>>> O preço da passagem é R$ 148,75."""

distancia = int(input('Digite a distância à ser percorrida:'))
preco_max = distancia * 0.85
preco_min = distancia * 0.57

if distancia <= 200:
    print(f'O preço da passagem é{preco_max:.2f}')
else: print(f'O preço da passagem é{preco_min:.2f}')

"""Faça um programa que leia um ano qualquer e mostre se ele é ou não bissexto. Pesquise as condições que fazem um ano ser ou não bissexto.
>>> 1900  → Não é bissexto
>>> 2020  → É bissexto
"""
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.") ## DÚVIDA -------------------------------------------------------------- !!!!!!

"""Faça um programa que leia dois números e mostre qual é o maior e o menor deles.
INPUT: Números: 4 e 19
>>> Maior: 19
>>> Menor: 4
"""
n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número'))
if n1>n2:
    print(f'O número {n1} é maior que {n2}')
else:
    print(f'O número{n1}é menor que {n2}')

"""
Faça um algoritmo que pergunte o salário de um funcionário e calcule o novo salário com aumento. Para salários de até R$ 1320,00, o aumento será de 15% e para salários superiores a R$ 1320,00 o aumento será de 10%.
INPUT: Salário = R$ 1000,00
>>> O salário com aumento é de: R$ 1150,00
INPUT: Salário = R$ 4400,78
>>> O salário com aumento é de: R$ 4840, 86
"""
sa = float(input('Informe seu salário atual:'))
amm = sa * 0.15
am = sa *0.10

if sa <= 1320:
    amm = sa * 0.15
    ar = sa + amm
    print(f'O seu aumento foi de R${amm:2f}, totalizando R$ {ar:.2f}')
elif sa >=1320:
    am = sa*0.10
    ar = sa + am
    print(f'O seu aumento foi de R${am:.2f}, totalizando R$ {ar:.2f}')

"""Desenvolva um programa que leia o comprimento de três retas e mostre se elas podem ou não formar um triângulo. DICA: Pesquise quais as condições de três retas formarem um triângulo.
INPUT: Lados = 5cm, 10cm e 9cm
>>> Os lados 5cm, 10cm e 9cm formam um triângulo!
INPUT: Lados = 1cm, 10cm e 9cm
>>> Os lados 1cm, 10cm e 9cm não formam um triângulo!
Para se formar um triângulo, a soma de dois lados devem ser maior do que o terceiro
"""
l1 = float(input('Digite o tamanho de uma das vértices'))
l2 = float(input('Digite o tamanho de outra vértice'))
l3 = float(input('Digite o tamanho de outra vértice'))

if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('É possível formar um triângulo')
else: print('Não é possível formar um triângulo')

"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
INPUT: n = 8984
>>> O número 8984 é positivo.
INPUT :n = -1
>>> O número -1 é negativo."""

neutro = int(input('Digite um número'))
if neutro > 0:
    print(f'O número {neutro} é positivo')
else: print(f'O número {neutro} é negativo.')

"""Faça um Programa que leia um número e em seguida mostre se o número é:
inteiro ou decimal;
positivo ou negativo;
par ou ímpar, somente se o número for inteiro e positivo
INPUT: n = 3.14
>>> O número 3.14 é decimal, positivo.
INPUT: n = 89
>>> O número 89 é inteiro, positivo e ímpar."""


n = float(input("Digite um número: "))
if n == int(n):
    tipo_de_numero = "inteiro"
else:
    tipo_de_numero = "decimal"

if n > 0:
    positivo = "positivo"
else:
    positivo = "negativo"

if tipo_de_numero == "inteiro" and positivo == "positivo":
    if int(n) % 2 == 0:
        par = "par"
    else:
        par = "ímpar"
else:
    par = ""

if par:
    resultado = f"O número {n} é {tipo_de_numero}, {positivo} e {par}."
else:
    resultado = f"O número {n} é {tipo_de_numero}, {positivo}."

print(resultado)


"""Faça um Programa que verifique se uma letra digitada é "A". Conforme a letra escrever: “A de amor”, “Letra inválida :(“
INPUT: texto = A
>>> A de amor
INPUT: texto = a
>>> A de amor
INPUT : batata
>>> batata não é A de amor."""

texto = input('Acerte a letra:')
if texto == "A" or texto == "a":
    print('A ou a de amor')
else:
    print('Batata não é A de amor')
"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante. O seu programa deve aceitar letras maiúsculas e minúsculas. Dica: pesquise como converter todo a string em caracteres minúsculos ou MAIÚSCULOS.
INPUT: letra = A ou a
>>> vogal
INPUT: letra = B ou b
>>> Consoante
"""
letra = input('Informe se a letra é vogal ou consoante:')
letra = letra.lower()
if letra in 'aeiou':
    print(f'A letra {letra} é uma vogal.')
else: 
    print(f'A letra {letra} é uma consoante.')
"""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
	INPUT: notas 10 e 6.5
>>> Aprovado
INPUT: notas 2 e 7.8
>>> Reprovado
"""
nota1= float(input('Digite sua nota de matemática:'))
nota2 = float(input('Digite sua nota de português:'))
media_nota = (nota1+nota2)/2

if media_nota > 6:
    print('Aprovado')
else:
    print('Reprovado')

    """Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool - R$ 3,80 por litro
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina R$ 4,70 por litro
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro 
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente. 
(gabarito na próxima página)
INPUT 1: A, 35 litros → O valor a pagar por 35 litros de álcool é R$ 126,35.
INPUT 2: G, 47 litros → O valor a pagar por 47 litros de gasolina é R$ 207,65.
INPUT 3: A, 12.5 litros → O valor a pagar por 12.5 litros de álcool é R$ 46,08.
INPUT 4: G, 4 litros → O valor a pagar por 35 litros de gasolina é R$ 18,05."""


preco_alcool = 3.80
preco_gasolina = 4.70
limite_desconto = 20
#desconto alcool_abaixo_limite = 0.03
#desconto alcool acima limite = 0.05
#desconto gasolina abaixo limite = 0.04
#desconto gasolina acima limite = 0.06

combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ")
litros_vendidos = float(input("Digite a quantidade de litros vendidos: "))

if combustivel == 'A' or combustivel == 'a':
    if litros_vendidos <= limite_desconto:
        valor_pago = litros_vendidos * (preco_alcool * (1 - 0.03))
    else:
        valor_pago = litros_vendidos * (preco_alcool * (1 - 0.05))
    print(f"O valor a pagar por {litros_vendidos:.2f} litros de álcool é R$ {valor_pago:.2f}.")
elif combustivel == 'G'or combustivel == 'g':
    if litros_vendidos <= limite_desconto:
        valor_pago = litros_vendidos * (preco_gasolina * (1 - 0.04))
    else:
        valor_pago = litros_vendidos * (preco_gasolina * (1 - 0.06))
    print(f"O valor a pagar por {litros_vendidos:.2f} litros de gasolina é R$ {valor_pago:.2f}.")
else:
    print("Tipo de combustível inválido.")

    """Faça um programa que faça 5 perguntas de sim ou não para uma pessoa sobre um crime. As perguntas são:
"Fez a matrícula na Infinity?"
"Está treinando programação além da sala de aula?"
"Fez o teste de lógica?"
"Entrega as atividades em dia?"
"Tá aprendendo a programar pelos dedos?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no aprendizado de Python. Se a pessoa responder positivamente a mais de 3 questões ela deve ser classificada como "Está no caminho certo para ser um excelente programador". Caso contrário, ele será classificado como "Precisa se dedicar mais.".

EXEMPLO 1:
"Fez a matrícula na Infinity?" Sim
"Está treinando programação além da sala de aula?" Sim 
"Fez o teste de lógica?" Sim 
"Entrega as atividades em dia?" Não
"Tá aprendendo a programar pelos dedos?" Sim
OUTPUT: Está no caminho certo para ser um excelente programador

EXEMPLO 2:
"Fez a matrícula na Infinity?" Não
"Está treinando programação além da sala de aula?" Não
"Fez o teste de lógica?" Não
"Entrega as atividades em dia?" Não
"Tá aprendendo a programar pelos dedos?" Sim
OUTPUT: Precisa se dedicar mais."""

q1 = input('Fez matrícula na infinity ?')
q2 = input('Está treinando programação além da sala de aula ?')
q3= input('Fez o teste de lógica?')
q4= input('Entrega as atividades em dia ?')
q5 = input('Tá aprendendo a programar pelos dedos ?')

pontuação = 0

while True:
    q1 = input('Fez matrícula na infinity ?')
    q2 = input('Está treinando programação além da sala de aula ?')
    q3= input('Fez o teste de lógica?')
    q4= input('Entrega as atividades em dia ?')
    q5 = input('Tá aprendendo a programar pelos dedos ?')

    if q1.upper() or q2.upper() or q3.upper() or q4.upper() or q5.upper()=='SIM':
        pontuação +1
    elif q1.upper() or q2.upper() or q3.upper() or q4.upper() or q5.upper()=='NÃO':
        pontuação +0
        break
    if pontuação >= 3:
        print('Está no caminho certo para ser um excelente programador')
    else: print('Precisa se dedicar mais')
    


        



    


    



