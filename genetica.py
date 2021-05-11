def RnaToProteinString(genome):
  triplets = [genome[i:i+3] for i in range(0, len(genome), 3)]
  codon = dict()
  codon["UUU"] = "F" 
  codon["CUU"] = "L"
  codon["AUU"] = "I"
  codon["GUU"] = "V"
  codon["UUC"] = "F"
  codon["CUC"] = "L"
  codon["AUC"] = "I"
  codon["GUC"] = "V"
  codon["UUA"] = "L"
  codon["CUA"] = "L"
  codon["AUA"] = "I"
  codon["GUA"] = "V"
  codon["UUG"] = "L"
  codon["CUG"] = "L"
  codon["AUG"] = "M"
  codon["GUG"] = "V"
  codon["UCU"] = "S"
  codon["CCU"] = "P"
  codon["ACU"] = "T"
  codon["GCU"] = "A"
  codon["UCC"] = "S"
  codon["CCC"] = "P"
  codon["ACC"] = "T"
  codon["GCC"] = "A"
  codon["UCA"] = "S"
  codon["CCA"] = "P"
  codon["ACA"] = "T"
  codon["GCA"] = "A"
  codon["UCG"] = "S"
  codon["CCG"] = "P"
  codon["ACG"] = "T"
  codon["GCG"] = "A"
  codon["UAU"] = "Y"
  codon["CAU"] = "H"
  codon["AAU"] = "N"
  codon["GAU"] = "D"
  codon["UAC"] = "Y"
  codon["CAC"] = "H"
  codon["AAC"] = "N"
  codon["GAC"] = "D"
  codon["UAA"] = "Stop"
  codon["CAA"] = "Q"
  codon["AAA"] = "K"
  codon["GAA"] = "E"
  codon["UAG"] = "Stop"
  codon["CAG"] = "Q"
  codon["AAG"] = "K"
  codon["GAG"] = "E"
  codon["UGU"] = "C"
  codon["CGU"] = "R"
  codon["AGU"] = "S"
  codon["GGU"] = "G"
  codon["UGC"] = "C"
  codon["CGC"] = "R"
  codon["AGC"] = "S"
  codon["GGC"] = "G"
  codon["UGA"] = "Stop"
  codon["CGA"] = "R"
  codon["AGA"] = "R"
  codon["GGA"] = "G"
  codon["UGG"] = "W"
  codon["CGG"] = "R"
  codon["AGG"] = "R"
  codon["GGG"] = "G"

  saidaa=[]
  for triplet in triplets:
    if codon.get(triplet, "X") == "Stop":
      return
    else:
      saidaa.append( codon.get(triplet, "X") )

  with open ('TESTE', 'w')  as Rna_file:
    Rna_file.write( ''.join(saidaa))  

with open('sequence_DNA.txt', 'r') as g_file:
  genome=g_file.read()
  lines=genome.splitlines()
  genome.replace('/n','')
  genome.replace('/r', '')
  genome.replace(lines[0], '')

RnaToProteinString(genome)