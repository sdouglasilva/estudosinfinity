# [LPIA-A01] Você está criando um programa para calcular a área de um retângulo. O programa deve solicitar ao usuário que forneça a base e a altura do retângulo. Em seguida, o programa deve calcular a área usando a fórmula:

# Área=Base×Altura

class FormasGeometricas:
  def __init__(self,nome,forma,tipo) -> None:
    self.nome = nome
    self.forma = forma
    self.tipo = tipo

  def calcularArea (self,base:float,altura:float):
    calcular = base * altura
    return calcular
  
class Retangulo(FormasGeometricas):
  def __init__(self, nome, forma, tipo) -> None:
    super().__init__(nome, forma, tipo)

retangulo = Retangulo('Retângulo','Retangular','retângulo')
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area_retangulo = retangulo.calcularArea(base,altura)
print(area_retangulo)
