from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

with open('Covid-19.txt','r') as g_file:
    a = g_file.read()
    
    lista = []
    
    cadeias=['Citosina', 'Timina', 'Guanina','Adenina']
    
    lista.append(a.count('C'))
    lista.append(a.count('T'))
    lista.append(a.count('G'))
    lista.append(a.count('A'))
    
    colors=['g', 'm', 'c', 'b']
plt.pie(lista, labels = cadeias, colors=colors,  
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0), 
        radius = 1.2, autopct = '%1.1f%%') 

plt.legend()
plt.show()

