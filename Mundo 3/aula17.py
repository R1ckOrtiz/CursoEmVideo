# Lista de estudantes e suas notas
estudantes = [
    {"nome": "Ana", "nota": 7.5},
    {"nome": "Carlos", "nota": 5.2},
    {"nome": "Beatriz", "nota": 8.7},
    {"nome": "Diego", "nota": 6.0},
    {"nome": "Eliana", "nota": 9.3}
]

# Função para calcular a média da turma
def calcular_media(estudantes):
    total_notas = sum([estudante["nota"] for estudante in estudantes])
    return total_notas / len(estudantes)

# Função para verificar aprovados e reprovados
def verificar_aprovacao(estudantes, nota_minima=6.0):
    aprovados = []
    reprovados = []
    for estudante in estudantes:
        if estudante["nota"] >= nota_minima:
            aprovados.append(estudante["nome"])
        else:
            reprovados.append(estudante["nome"])
    return aprovados, reprovados

# Calculando a média da turma
media_turma = calcular_media(estudantes)
print(f"Média da turma: {media_turma:.2f}")

# Verificando aprovados e reprovados
aprovados, reprovados = verificar_aprovacao(estudantes)

print("\nEstudantes aprovados:")
for nome in aprovados:
    print(nome)

print("\nEstudantes reprovados:")
for nome in reprovados:
    print(nome)
