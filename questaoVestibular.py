nome = ""
nota = 0.0


maior_nota_todas = 0
nome_maior_nota = ""
aprovados = 0

maior_nota_turma_a = 0
aprovados_turma_a = 0
for a in range (2):
    nome = input("Digite seu nome: ")
    nota = float(input("Digite sua nota: "))

    if nota>maior_nota_turma_a:
        maior_nota_turma_a = nota
        if maior_nota_turma_a>maior_nota_todas:
            maior_nota_todas = maior_nota_turma_a
            nome_maior_nota = nome
        if nota >= 7:
            aprovados += 1
            aprovados_turma_a += 1


maior_nota_turma_b = 0
aprovados_turma_b = 0
for b in range (2):
    nome = input("Digite seu nome: ")
    nota = float(input("Digite sua nota: "))

    if nota>maior_nota_turma_b:
        maior_nota_turma_b = nota
        if maior_nota_turma_b>maior_nota_todas:
            maior_nota_todas = maior_nota_turma_b
            nome_maior_nota = nome
        if nota >= 7:
            aprovados += 1
            aprovados_turma_b += 1

maior_nota_turma_c = 0
aprovados_turma_c = 0
for c in range (2):
    nome = input("Digite seu nome: ")
    nota = float(input("Digite sua nota: "))

    if nota>maior_nota_turma_c:
        maior_nota_turma_c = nota
        if maior_nota_turma_c>maior_nota_todas:
            maior_nota_todas = maior_nota_turma_c
            nome_maior_nota = nome
        if nota >= 7:
            aprovados += 1
            aprovados_turma_c += 1

maior_nota_turma_d = 0
aprovados_turma_d = 0
for c in range (2):
    nome = input("Digite seu nome: ")
    nota = float(input("Digite sua nota: "))

    if nota>maior_nota_turma_d:
        maior_nota_turma_d = nota
        if maior_nota_turma_d>maior_nota_todas:
            maior_nota_todas = maior_nota_turma_d
            nome_maior_nota = nome
        if nota >= 7:
            aprovados += 1
            aprovados_turma_d += 1

print("Quantidade de aprovados: ", aprovados,"\n"
                                             
        "Aprovados na turma A: ", aprovados_turma_a, "\n"
        "Aprovados na turma B: ", aprovados_turma_b, "\n"
        "Aprovados na turma C: ", aprovados_turma_c, "\n"
        "Aprovados na turma D: ", aprovados_turma_d, "\n\n"
                                                     
        "Maior nota na turma A: ", maior_nota_turma_a, "\n"
        "Maior nota na turma B: ", maior_nota_turma_b, "\n"
        "Maior nota na turma C: ", maior_nota_turma_c, "\n"
        "Maior nota na turma D: ", maior_nota_turma_d, "\n\n"
                                                       
        "ALUNO COM A MAIOR NOTA: ", nome)
