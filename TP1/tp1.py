data_dict = {} # (column , atleta_id) -> data

file = open("emd.csv", "r")

header = file.readline().rstrip('\n')
column_names = header.split(",")

for line in file:
    data = line.rstrip('\n').split(",")
    if len(data) != len(column_names):
        print("Invalid line: " + line)
        continue
    for i in range(len(data)):
        data_dict[(column_names[i], data[0])] = data[i]

file.close()

modalidades = set()
for (column, atleta_id) in data_dict:
    if column == "modalidade":
        modalidades.add(data_dict[(column, atleta_id)])
modalidades = sorted(modalidades)

aptos = 0
inaptos = 0
for (column, atleta_id) in data_dict:
    if column == "resultado":
        if data_dict[(column, atleta_id)] == "true":
            aptos += 1
        else:
            inaptos += 1
percentagem_aptos = aptos / (aptos + inaptos) * 100
percentagem_inaptos = inaptos / (aptos + inaptos) * 100

file = open("resultados.txt", "w")

file.write("Modalidades: " + ", ".join(modalidades) + "\n\n")
file.write("Aptos: " + str(aptos) + " (" + str(percentagem_aptos) + "%)\n\n")
file.write("Inaptos: " + str(inaptos) + " (" + str(percentagem_inaptos) + "%)\n\n")

escaloes = {} # escalão -> lista de atletas
for (column, atleta_id) in data_dict:
    if column == "idade":
        idade = int(data_dict[(column, atleta_id)])
        escalao = (idade // 5) * 5
        nome_atleta = data_dict[("nome/primeiro", atleta_id)] + " " + data_dict[("nome/último", atleta_id)]
        if escalao not in escaloes:
            escaloes[escalao] = []
        escaloes[escalao].append(nome_atleta)

file.write("Atletas por escalão:\n")
for escalao in sorted(escaloes):
    total_atletas_esc = len(escaloes[escalao])
    percentagem_esc = total_atletas_esc / (aptos + inaptos) * 100
    file.write(f"Escalão {escalao} - {escalao + 4} ({total_atletas_esc} - {percentagem_esc:.2f}%):\n")
    for atleta in escaloes[escalao]:
        file.write(f"- {atleta}\n")
    file.write("\n")

file.close()

print("Resultados guardados no ficheiro 'resultados.txt'")
