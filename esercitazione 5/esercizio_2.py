import numpy as np 
import sys,os
import pandas as pd

sys.path.append('~/Scrivania/metodi computazionali/esercizi-corso-metodi/esercitazione 5/reco.py')
import reco

hit0='~/Scrivania/metodi computazionali/get-mcf-data/percrso/cartella/esercitazione/hit_times_M0.csv'
hit1='~/Scrivania/metodi computazionali/get-mcf-data/percrso/cartella/esercitazione/hit_times_M1.csv'
hit2='~/Scrivania/metodi computazionali/get-mcf-data/percrso/cartella/esercitazione/hit_times_M2.csv'
hit3='~/Scrivania/metodi computazionali/get-mcf-data/percrso/cartella/esercitazione/hit_times_M3.csv'

def r_file(hf):
	pd.read_csv(hf)
