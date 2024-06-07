# [LPIA-A02] Crie um programa em Python para verificar se um número é positivo, negativo ou zero. O programa deve solicitar ao usuário que insira um número e, em seguida, imprimir uma mensagem indicando a natureza do número.

# Se o número for maior que zero, exiba a mensagem "O número é positivo." Se for menor que zero, exiba "O número é negativo." Caso seja zero, a mensagem deve ser "O número é zero."

#TrainningFunction

def classifica_numero(num):
  if num < 0:
    return f'O número: {num} é negativo'
  if num > 0:
    return f'O número: {num} é positivo'
  else:
    return f'O número é 0, neutro.'
  
numero = int(input('Digite um número'))
print(classifica_numero(numero))