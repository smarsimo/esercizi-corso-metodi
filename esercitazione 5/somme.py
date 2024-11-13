import numpy as np
"""
def somma(*args):

	#Funzione che restituisce la somma dei primi n numeri naturali
	
	sum=0
	for i in range(args[0]+1):
		sum=sum+i
	return sum
	
#definisco una funzione che restituisca la somma delle radici dei primi 
#n numeri naturali con n da passare tramite un argomento

def somma_radici(*args):
	
	#Funzione che restituisce la somma delle radici dei primi n numeri 
	#naturali 

	sum=0
	for i in range(args[0]+1):
		sum=sum+np.sqrt(i)
	return sum

"""

def som_prod(*args):
	
	#funzione che restituisce somma e prodotto dei primi n numeri naturali
	
	sum=0
	prod=1
	for i in range(args[0]):
		sum=sum+(i+1)
		prod=prod*(i+1)
	return sum, prod
	

def sommatoria(*args, **kwargs):
	#funzione che restituisce la somma per i che va da 0 a n
	#di i^alpha
	#--------------
	#PARAMETRI:
	#n: numero al quale si ferma la sommatoria
	#alpha: esponente con valore di default uguale a 1
	alpha=1
	sommatoria=0
	for i in range(args[0]+1):
		sommatoria=sommatoria+pow(i,alpha)
	return sommatoria

	
	









