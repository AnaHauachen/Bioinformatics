pattern = input()
g = open("FASTA.txt", "r")
genome = g.read()
lines=genome.splitlines()
genome=genome.replace("/n","")
genome=genome.replace(lines[0],"")
posicao= genome.find(pattern)
while posicao !=-1:
    print(posicao, end=' ')
    posicao = genome.find(pattern, posicao+1, len(genome)) #1.1 encontrar as posições
    
a=genome.replace('A','t')
b=a.replace('T','a')
c=b.replace('G','c')
d=c.replace('C','g')
e=d.upper()
f = e[::-1]
print(f) #1.2 complementar

 

conta=(str(genome.count('A')), str(genome.count('T')), str(genome.count('C')), str(genome.count('G'))) #1.3 contar o número de ocorrências
print(conta)

 

rep=(genome.replace('T','U')) #1.4 RNA
print(rep)

 

output = open("results.text", "w")
output.write(str(posicao) + '/n')
output.write(str(f) + '/n')
output.write(str(conta) +'/n')
output.write(str(rep)+ '/n')