arq = open('GDS5.txt', 'r')

soma=0
N_element_Col=0


for linha in arq:
    columns=linha.strip().split("\t")
    #print (columns[4])

    if columns[3] !=  "null":
        N_element_Col=N_element_Col+1
        soma= soma + float(columns[3])
print('Média de Colunas é: ', soma/N_element_Col)



