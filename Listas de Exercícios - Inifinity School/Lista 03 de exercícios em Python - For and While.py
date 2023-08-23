""""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0 e após o 0 mostre “BOOOM!”."""

tempo_espera = 10

while tempo_espera > 0:
    print(tempo_espera)
    tempo_espera-=1 
print('BOOM!!!')

#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

for i in range(1,50):
    if i %2==0:
        print(i)

#Crie um programa que mostre na tela a soma de todos os números pares que estão no intervalo entre 1 e 50.

for i in range(1,50):
    if i %2==0:
        soma= i +i
        print(soma)

#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

par = 0
impar = 0

for i in range (0,10):
    n1 = int(input('Digite um número'))
if n1 % 2 == 0:
    par += 1
else:
    impar +=1
print (f'A quantidade de números impares é igual à {impar}, e a quantidade de números pares é igual à {par}')

#Refaça o exercício da tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número para saber sua tabuada'))

for i in range (1,11):
    resultado = num*i
    print(f'A tabuada do número {num}, é {num}x{i}={resultado}')

'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares e quantos números pares foram informados. Se o valor digitado for ímpar, desconsidere-o na soma. Não crie uma variável para cada número nesse exercício.'''

par = 0
impar = 0
soma = 0
for i in range (1,7):
    n1 = int(input(f'Digite O {i}º um número'))
    if n1 % 2 == 0:
        par += 1
        soma += n1
    else:
        impar+=1
print (f'A quantidade de números impares é igual à {impar}, e a quantidade de números pares é igual à {par}, a soma dos números pares existentes é {soma}')

'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
n1 = int(input('Digite o primeiro termo da P.A. : '))'''

razao = int(input('Digite a razão da P.A. : '))

decimo = n1 + (10 - 1) * razao #10 - 1 pois vc quer achar o decimo termo, essa é a formula matematica

for c in range(n1,decimo + razao, razao):
    formula = n1 + razao

    print(c, end=' --> ')

'''Faça um programa que leia um número positivo e diga se ele é ou não um número primo. O programa deverá mostrar quantas vezes o número foi divisível.'''

n1 = int(input('Digite um número:'))
if n1<=1:
    print('Este é um número não é primo:')
else:
    divisivel = 0
    for i in range(2,n1):
        if n1 %i==0:
            divisivel+=1
    if divisivel ==0:
        print(f'{n1} um número primo')
    else:
        print(f'{n1} não é um número primo e foi divisível {divisivel} vezes.')

'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = input("Digite uma frase: ")

frase_sem_espacos = ""
for caractere in frase:
    if caractere != " ":
        frase_sem_espacos += caractere

frase_formatada = frase_sem_espacos.upper()

if frase_formatada == frase_formatada[:-1]:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")

'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. Não crie uma variável para cada ano de nascimento de cada pessoa.'''

maioridade = 0
menoridade = 0

for i in range(0,7):
    anodenascimento = int(input('Digite o ano de nascimento:'))
    idade = 2023 - anodenascimento
    if idade >= 18:
        maioridade += 1
        print(f'Você é maior de idade')
    else:
        menoridade += 1
        print(f'Você é menor de idade')
print(f'Existem {maioridade} maiores, e {menoridade} menores')

'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. Utilize for sem criar uma variável para o peso de cada uma das pessoas.'''

maior_peso = 0
menor_peso = 0

for i in range(5):
    peso = float(input("Digite o peso em kg: "))

    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso

print(f"Maior peso :, {maior_peso}, kg")
print(f"Menor peso :, {menor_peso}, kg")

'''Faça um programa que conte de 1 até o número do usuário, determine o menor valor, o maior valor e a soma dos valores. Faça que o programa receba apenas números entre 0 e 1000.'''

n1 = int(input('Digite um número'))
menor = None
maior = 0
soma = 0

while n1 < 0 or n1 >1000:
    print('Numero fora do intervalo permitido. Digite um número de 0 à 1000.')
    n1 = int(input('Digite um número'))

menor = None
maior = 0
soma = 0
for n2 in range (1,n1+1):
    soma+=n2
    if menor is None or n2 < menor:
        menor = n2
    if n1 > maior   :
        maior = n2
        print(f'maior = {maior}')

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")

'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120'''

numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}.")

'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''

lula=0
bozo =0
klaus=0
votar = None
for i in range(1000000):
    votar = int(input('Para votar em Lula, tecle {1}. Para bozo tecle {2}. Para Klaus tecle{3}Para finalizar o processo tecle{4}'))    
    while votar<=0 or votar>4:
        print('Insira o número correspondente ao seu candidato.')
        votar = int(input('Para votar em Lula, tecle {1}. Para bozo tecle {2}. Para Klaus tecle{3}Para finalizar o processo tecle{4}'))
    if votar == 1:
        lula +=1
        print('Voto computado com sucesso, Lula para presidente !')
    if votar == 2:
        bozo +=1
        print('Voto computado com sucesso, Bozo para presidente !')
    if votar == 3:
        klaus +=1
        print('Voto computado com sucesso, Klaus para presidente !')
    if votar == 4:
        print('Nesta seção temos um total de,',bozo+lula+klaus,f'votos, sendo {lula} de Lula, {bozo} de Bozo e {klaus} de Klaus.')

'''O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50'''

quantidade = int(input('Digite a quantidade do item para exibir a tabela de preços:'))
valor_final = quantidade * 1.99
    
for i in range(1,50):

        print(f'Deverá ser pago pelo cliente:{quantidade+i}- item - R${(quantidade+i)*1.99}')






