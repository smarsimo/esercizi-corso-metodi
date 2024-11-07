import numpy as np

def somma(*args):
	"""
	Funzione che restituisce la somma dei primi n numeri naturali
	"""
	
	sum=0
	for i in range(args[0]+1):
		sum=sum+i
	return sum
	
#definisco una funzione che restituisca la somma delle radici dei primi 
#n numeri naturali con n da passare tramite un argomento

def somma_radici(*args):
	"""
	Funzione che restituisce la somma delle radici dei primi n numeri 
	naturali 
	"""
	sum=0
	for i in range(args[0]+1):
		sum=sum+np.sqrt(i)
	return sum

