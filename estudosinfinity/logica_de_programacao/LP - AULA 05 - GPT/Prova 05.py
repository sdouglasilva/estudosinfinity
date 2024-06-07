
def calcular_media_e_status(notas):
    media = sum(notas) / len(notas)
    status = "Aprovado" if media >= 7.0 else "Reprovado"
    return media, status

num_alunos = int(input("Digite o número de alunos: "))

soma_medias = 0

for i in range(1, num_alunos + 1):
    print(f"\nAluno {i}:")
    nome = input("Digite o nome do aluno: ")
    notas = []
    for j in range(1, 4):
        nota = float(input(f"Digite a nota {j} do aluno {nome}: "))
        notas.append(nota)
    
    media, status = calcular_media_e_status(notas)
    soma_medias += media
    
    print(f"\nNome do aluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")

media_geral = soma_medias / num_alunos
print(f"\nMédia geral da turma: {media_geral:.2f}")
