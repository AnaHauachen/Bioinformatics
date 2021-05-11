from modeller import *
from modeller.automodel import *

log.verbose()
env=environ()

env.io.atom_files_directory= ["C:/Users/Utilizador/Documents/Bioinfo"]

env.io.hetatm=True
env.io.water=True

a=automodel(env, alnfile="alinha.pir",knowns = '4HPG.fasta', sequence = 'bgl') 
a.starting_model = 1 
a.ending_model = 5 
a.make() 