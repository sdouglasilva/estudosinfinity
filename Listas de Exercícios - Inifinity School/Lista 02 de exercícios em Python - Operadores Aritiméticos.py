"""LISTA DE EXERCÍCIOS LÓGICA DE PROGRAMAÇÃO
⚠️OBS: 
Os três sinais de maior “>>>” significam somente que o resultado está no terminal.
INPUT é o que o usuário digita.
OUTPUT é o que é mostrado na tela (terminal)"""

"""Faça um programa que mostre a mensagem "Alô mundo" na tela.
>>> Alô mundo"""

print('Hello World')

"""Faça um Programa que peça um número e exiba o seu antecessor e sucessor.
INPUT: 7
OUTPUT: >>> O número 7 tem o antecessor 6 e o sucessor 8."""

numero = int(input("Digite um número"))

antecessor = numero - 1
sucessor = numero + 1

print(f'O antecessor do número {numero} é {antecessor}, o sucessor do número {numero}, é {sucessor}')

"""Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
INPUT: 7
OUTPUT: >>> O número informado foi 7."""

outro_numero = int(input("Dígite outro número"))
print(f'O número informado foi:{outro_numero}')

""""Faça um Programa que peça dois números e imprima a soma.
INPUT: 4 e 5
OUTPUT: >>> 4 + 5 = 9."""

n1 = int(input('Digite um número'))
n2 = int(input('Digite outro número'))
soma = n1+n2
print(f'A soma entre os números digitados é:{n1}+{n2}={soma}')

"""Faça um Programa que peça as 4 notas bimestrais e mostre a média.
INPUT: 4, 5.5, 10 e 9.7
OUTPUT: >>> Média bimestral = 7.3"""

nota1 = int(input('Digite sua nota no primeiro bimestre:'))
nota2 = int(input('Digite sua nota no primeiro bimestre:'))
nota3 = int(input('Digite sua nota no primeiro bimestre:'))
nota4 = int(input('Digite sua nota no primeiro bimestre:'))
media = float(nota1+nota2+nota3+nota4) / 4

print(f'Sua média anual é {media}')

""""Faça um Programa que converta metros para centímetros.
INPUT: 1 m
OUTPUT: >>> 1 m = 100 cm
"""

m = int(input('Digite o seu tamanho em metros'))
cm = m * 100
print(f'Seu tamanho em metros é{cm}cm')

"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
INPUT: 170.99
OUTPUT: >>> O novo preço do produto de 170.99 com 5% de desconto é R$ 162,44"""

preço_produto = float(input("Informe o preço do produto:"))
desconto = (preço_produto * 0.05)
preço_final = preço_produto - desconto
print(f'Seu produto com desconto é {preço_final}')

"""Faça um Programa que peça o raio de um círculo, em centímetros, calcule e mostre sua área. Considere pi = 3
INPUT: raio =  5
OUTPUT: >>> A área do círculo de raio 5 cm = 75 cm²"""

raio = int(input('Informe o raio desejado'))
area = 3 * (raio ** 2)
print(f'A área à ser contruída é:{area}m²')


"""Faça um Programa que calcule a área de um círculo, em centímetros, em seguida mostre o dobro desta área para o usuário.
INPUT: 5
OUTPUT: >>> O dobro da área do círculo de raio 5 cm = 150 cm²"""


raio = int(input('Informe o raio desejado'))
area = 3 * (raio ** 2)
dobro_area = area * 2
print(f'O dobro área à ser contruída é:{dobro_area}m²')

"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
INPUT: valor_hora = 10 e numero_horas = 220
OUTPUT: >>> O salário do mês é R$ 2200,00.
"""

valor_hora = float(input('Informe seu rendimento por hora: '))
numero_horas = int(input('Informe o número de horas trabalhadas por mês: '))
salario_mes = valor_hora * numero_horas
print(f'O seu salário do mês é R${salario_mes:.2f}')

"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. Fórmula: C = 5 * ((F-32) / 9).
INPUT: 75 ºF
OUTPUT: >>> 75 ºF = 23,88888 ºC
"""
fahrenheit = float(int('Digite a temperatura em Fahrenheit'))
celsius = 5 * ((fahrenheit-32)) / 9
print(f'{fahrenheit}ºF = {celsius} ºC')

"""""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
INPUT: n1 = 10, n2 = 5 e n3 = 3.14
OUTPUT: >>> 
o produto do dobro do primeiro com metade do segundo = 22.5
a soma do triplo do primeiro com o terceiro = 33.14
o terceiro elevado ao cubo = 30.959144
"""

n1 = int(input('Digite um número inteiro'))
n2 = int(input('Digite outro número inteiro'))
n3 = float(input('Digite um número real'))
n1_1 = (n1*2)+(n2/2)
n1_2 = (n1*3) + n3
n3_1 = n3 **3
print(f'O produto do dobro do primeiro com metade do segundo = {n1_1}. Já a soma do triplo do primeiro com o terceiro = {n1_2}. O terceiro elevado ao cubo ={n3_1}')

"""Tendo como dados de entrada a altura de uma pessoa, em centímetros, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura em metros) - 58
INPUT: altura = 180 cm
OUTPUT: >>> Peso ideal para uma pessoa de 1.80 m é 72.86 kg
"""

altura = float(input('Digite sua altura em metros:'))
peso_ideal = (72.7*altura) - 58
print(f'Seu peso ideal em relação à sua altura é {peso_ideal}')

"""Faça um programa que peça o tamanho de um arquivo para download (em MB, megabytes) e a velocidade de um link de Internet (em Mbps, megabits por segundo), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). Considere que 1 byte = 8 bits
INPUT: tamanho do arquivo = 500 MB e velocidade de 10 Mbps
OUTPUT: >>> O tempo aproximado de download é de 6.67 minutos"""

t_a = float(input('Digite o tamanho do arquivo em mb'))
v_b = float(input('Digite a velocidade do link de internet:'))
conversor = t_a * 8 #4000
mbps= conversor / v_b #400
tempo_download = mbps / 60
print('O tempo de download do arquivo é de{tempo_download} minutos')


"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
		
Gabarito:
+ Salário Bruto : R$ 1000,00
- IR (11%) : R$ 110,00
- INSS (8%) : R$ 80,00
- Sindicato ( 5%) : R$ 50,00
= Salário Liquido : R$ 760,00
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
ganhos_hora = float(input('Digite quanto você ganha por hora: '))
hora_mes = int(input('Digite o número de horas trabalhadas no mês ;'))
salario_bruto = ganhos_hora * hora_mes
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindi = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindi
print(f'Seu salário bruto é R${salario_bruto:.2f}. No entanto, possuem alguns descontos, tais como: IR - R${ir:.2f}, INSS - R${inss:.2f} e Sindicato - R${sindi:.2f}. Sendo assim, seu salário líquido é de - R${salario_liquido:.2f}')

"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.
INPUT: Tamanho da área = 420 m²
OUTPUT: >>> Você precisará de comprar 8 latas de tintas no valor de R$ 640.00
"""

"""area_marcada = int(input('Informe o tamanho em m² da área a ser pintada:'))
qtdade_tinta = area_marcada // 3
qtdade_fr= qtdade_tinta // 18
valor_total = qtdade_fr *80
print(f'Você precisará comprar {qtdade_fr}, no valor de R${valor_total:.2f}') ------------------------ DÚVIDA  -------------"""



"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em galões de 18 litros, que custam R$ 80,00 ou em latinhas de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 2 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;

INPUT: Tamanho da área = 570 m²
OUTPUT: >>> Você precisará de comprar 6 galões de tintas no valor de R$ 420.00 ou 27 latinhas de tinta no valor de R$ 675.00.
"""
area_delimitada = int(input('Informe a área a ser pintada:'))
tinta_necessaria = -(-area_delimitada // 6)
qtade_gl = -(-tinta_necessaria // 18)
vt_gl= qtade_gl * 80
qtdade_lt = -(-tinta_necessaria // 3.6)
vt_lt = tinta_necessaria * 25
print(f'Você precisará comprar {qtade_gl} galões de tinta no valor de R$ {vt_gl:.2f}, ou {qtdade_lt} latinhas de tinta no valor de R${vt_lt:.2f}')

"""Solicitar a idade de uma pessoa em dias e informar na tela a idade em anos, meses e dias.
INPUT: 15 000
OUTPUT: >>> 15 000 dias = 41 anos, 1 mês e 5 dias
"""

idade_dias = int(input("Digite a idade em dias: "))
anos = idade_dias // 365
meses = (idade_dias % 365) // 30
dias = (idade_dias % 365) % 30
print(f"{idade_dias} dias = {anos} anos, {meses} meses e {dias} dias.")

"""Faça um algoritmo que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias que ele ficou com o veículo. Calcule o preço a pagar pelo aluguel, sabendo que o carro custa R$100 por dia e R$0,75 por km rodado.
Ex: INPUT: 1000 km rodados e 8 dias.
OUTPUT >>> O valor do aluguel é de R$ 1550,00. 
"""
km_rodados = int(input('Informe a quilometragem utilizada:'))
diarias = int(input('Informe a quantidade de diárias'))
vt_km_rodados = km_rodados * 0.75
vt_diarias = diarias *100
vt = vt_km_rodados + vt_diarias
print(f'O valor total de do aluguel é de R${vt:.2f}')


"""Faça um algoritmo que leia um número inteiro qualquer e mostre na tela sua tabuada. 
Ex: n = 3


3 x 1 = 3 
3 x 2 = 6 
3 x 3 = 9 
3 x 4 = 12 
3 x 5 = 15


3 x 6 = 18 
3 x 7 = 21 
3 x 8 = 24 
3 x 9 = 27 
3 x 10 = 30"""

numero = int(input("Digite um número inteiro: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo e que calcule e mostre o comprimento da hipotenusa.
INPUT: Cateto oposto = 3 e cateto adjacente = 4
OUTPUT >>> A hipotenusa é 5."""


cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5

print(f"A hipotenusa é {hipotenusa}.")

"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: INPUT número = 9847
OUTPUT >>> Unidade: 7 Dezena: 4 Centena: 8 Milhar: 9
"""

numero = int(input("Digite um número de 0 a 9999: "))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print(f"Unidade: {unidade} Dezena: {dezena} Centena: {centena} Milhar: {milhar}")




























