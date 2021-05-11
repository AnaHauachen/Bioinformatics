import csv

with open('GDS5.txt') as csvfile:
  lines = csv.reader(csvfile, delimiter='\t')

  for index, line in enumerate(lines):
    # remove as duas primeiras colunas
    del line[0:2]

    soma = 0
    for value in line:
      soma += float(value)
    
    media = soma/len(line)

    print( 'Media da linha {} é: {}'.format(index+1, media ) )
