import csv

def conteUdoAT(sequence):
    length=len(sequence)
    a_count=sequence.upper().count('A')
    t_count=sequence.upper().count('T')
    at_content=(a_count + t_count)/length
    return at_content
arq = open('data.csv', 'r')
texto = arq.readlines()
for linha in texto :
    col=linha.strip().split(",")
    species_name=col[0]
    sequence=col[1]
    gene_name=col[2]
    expression_level=float(col[3])

   #A
   print(species_name, gene_name)
#---------------------------------------------------
#B
    if species_name == "Drosophila simulans" or species_name=="Drosophila melanogaster":
        print(gene_name)

#-------------------------------------------------
 #C
    for i in range(90,110):
        if len(sequence)==i:
            print(gene_name)
#------------------------------------------------------
#D

    for nome in gene_name:
       if species_name!='Drosophila melanogaster':
            if (nome[0] == 'h') or (nome[0]=='k'):
               print (gene_name)
#--------------------------------------------------------
#E

    if expression_level > 200 and conteUdoAT(sequence) <0.5:
       print(gene_name)

#--------------------------------------------------------------------

#F
  if conteUdoAT(sequence)< 0.45:
       print (gene_name,'Baixo')
    elif conteUdoAT(sequence)>0.65:
        print(gene_name, 'Alto')
    else:
        print(gene_name,'médi
#--------------------------------------------------------------------

#G      

    if expression_level < 90:
        print(gene_name,'Negligenciado')
    elif expression_level > 90 and expression_level < 200:
        print(gene_name,'Baixo')
    elif expression_level > 200 and expression_level < 300:
        print(gene_name,'Normal')
    else:
        print(gene_name,'Alto')
#--------------------------------------------------------------------

 #H       
saida = (' Drosophila virilis, CTACTGTTAATGCTATGGACAGATGTGTGTGCGCTGTTTGCTTGTGGCTAAAATAAGT GTTAACGGAAAA, Dvir\GJ13080, 123')
with open ('data.txt', 'a')  as R_file:
    R_file.write(saida)
#--------------------------------------------------------------------
