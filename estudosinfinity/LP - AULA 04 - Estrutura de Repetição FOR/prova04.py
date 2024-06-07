# [LPIA-A04] Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).

# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso


numero = int(input('Digite o menor número'))
numero2 = int(input('Digite o maior número:'))

soma = 0
for i in range(numero, numero2 +1):
  print(i)
  if i %2==0:
    soma += i

if soma != 0:
    print("A soma dos números pares no intervalo é:", soma)
else:
    print("Não há números pares no intervalo.")#A única saída possível onde caíriamos nesse bloco é um intervalo ao qual não existe um intervalo....(1,1)