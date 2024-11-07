import sys,os
import numpy as np

sys.path.append('~/Scrivania/metodi	computazionali/esercizi-corso-metodi/somme.py')
import somme 

n=input('inserisci un numero n: ')
nn=int(n)
print('somma dei primi', nn, 'numeri:', somme.somma(nn))
print('somma delle radici dei primi', nn, 'numeri:', somme.somma_radici(nn))


