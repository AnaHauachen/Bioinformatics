s2 = " ".upper()
s1 = " ".upper()
       
linhas = int(len(s1))
colunas = int(len(s2))

M = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(" ")
    M.append(linha)

for i in range(linhas):
    for j in range(colunas):
        if s1[i] == s2[j]:
                M[i][j] = "*"

print("  ",s2)
for i in range(linhas):
    print(s1[i], " ", end = "")
    for j in range(colunas):
        print(M[i][j], end ="")
    print()
