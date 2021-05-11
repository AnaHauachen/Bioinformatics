c=input()
saida=[]

with open('FASTA.txt','r') as g_file:
  genome = g_file.read()
  lines = genome.splitlines()
  genome.replace('\n', '')
  genome.replace( lines[0], '' )

for i in range (len(genome)):
  if genome[i:i+len(c)] == c:
    saida.append(i)


with open('saida', 'w') as f:
  f.write( ' '.join( map(str, saida) ) )