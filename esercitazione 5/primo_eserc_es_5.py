import sys,os
import numpy as np

sys.path.append('~/Scrivania/metodi	computazionali/esercizi-corso-metodi/somme.py')
import somme 

n=input('inserisci un numero n: ')
esp=input('inserisci un esponente: ')
exp=int(esp)
nn=int(n)
"""
print('somma dei primi', nn, 'numeri:', somme.somma(nn))
print('somma delle radici dei primi', nn, 'numeri:', somme.somma_radici(nn))
"""
#chiamo anche le funzioni introdotte dall'esercizio 1 della quinta
#esercitazione

s=somme.som_prod(nn)
print('somma dei primi', nn, 'numeri:', s[0])
print('prodotto dei primi', nn, 'numeri:', s[1])
Sum=somme.sommatoria(nn,alpha=exp)
print('la somma dei primi', nn, 'numeri elevati alla', exp, 'è:', Sum)

