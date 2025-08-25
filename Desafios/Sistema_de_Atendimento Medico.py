# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# 1ª ordenação: ordenar urgentes por idade decrescente, manter ordem dos demais
def urgentes_por_idade(paciente):
    nome, idade, status = paciente
    # Para urgentes, -idade para ordem decrescente, para outros retorna 0 (fica na frente ou no meio, não altera)
    if status == "urgente":
        return -idade
    else:
        return 0

pacientes.sort(key=urgentes_por_idade)

# 2ª ordenação: ordenar por prioridade urgente=0, idoso=1, normal=2
def prioridade(paciente):
    nome, idade, status = paciente
    if status == "urgente":
        return 0
    elif idade >= 60:
        return 1
    else:
        return 2

pacientes.sort(key=prioridade)

# Exibe a ordem de atendimento
print("Ordem de Atendimento: " + ", ".join([p[0] for p in pacientes]))
