# [LP-A01] A partir do que aprendemos até agora:
# Crie um exemplo de cada uma das principais tipagens de variáveis.
# Crie uma solicitação de dados ao usuário.
# Imprima a solicitação anterior na tela com uma mensagem personalizada.
#TrainningPOO
class CadastrarMonitor:
  def __init__(self, nome:str,idade:int,peso:float,estado_Civil:bool):
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.estado_Civil = estado_Civil

nome = input('Digite seu nome')
idade = int(input('Digite sua idade'))
peso = float(input('Digite seu peso'))
estado_Civil = input('Se for solteiro digite[s], caso seja casado digite[c]')

if estado_Civil == 'c':
  estado_Civil = True
else:
  estado_Civil = False

cadastro = CadastrarMonitor(nome,idade,peso,estado_Civil)

print("Cadastro:")
print("Nome:", cadastro.nome)
print("Idade:", cadastro.idade)
print("Peso:", cadastro.peso)
print("Estado Civil:", "Casado" if cadastro.estado_Civil else "Solteiro")

print(type(cadastro.nome))
print(type(cadastro.idade))
print(type(cadastro.peso))
print(type(cadastro.estado_Civil))
