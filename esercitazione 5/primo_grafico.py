import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#leggo i file forniti dal professore 
hit0=pd.read_csv('~/Scrivania/metodi computazionali/get-mcf-data/percrso/cartella/esercitazione/hit_times_M0.csv')
hit1=pd.read_csv('~/Scrivania/metodi computazionali/get-mcf-data/percrso/cartella/esercitazione/hit_times_M1.csv')
hit2=pd.read_csv('~/Scrivania/metodi computazionali/get-mcf-data/percrso/cartella/esercitazione/hit_times_M2.csv')
hit3=pd.read_csv('~/Scrivania/metodi computazionali/get-mcf-data/percrso/cartella/esercitazione/hit_times_M3.csv')

#produco un istogramma dei tempi per il modulo 0
"""
n,bins,p=plt.hist(hit0['hit_time'], bins=100, range=(280000,1000000000),color='gold',alpha=0.7)
plt.xlabel('tempi')
plt.show()
"""

#produco un istogramma delle differenze dei tempo fra hit consecutivi
Deltat0_1=(hit1['hit_time']-hit0['hit_time'])
dtmask=Deltat0_1>0
logmask=np.log(Deltat0_1[dtmask])
n,bins,p=plt.hist(logmask,bins=100)
plt.xlabel(r'$log_{10}(\Delta t)$ [ns]')
plt.show()

