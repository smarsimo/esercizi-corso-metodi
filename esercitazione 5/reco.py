import numpy as np

class Hit():
	"""
	classe per rappresentare i sensori colpiti
	
	Parametri
	-------------------------------------------
	
	mod_id : modulo
	det_id : sensore
	time   : time Stamp rivelazione
	"""
	
	def __init__(self, mod_id, det_id, time):
		self.mid    = mid 
		self.sid    = sid
		self.time   = time
	
	def __eq__(self,other):
		return self.time == other.time
		
	def __lt__(self,other):
		if self.time == other.time:
			return 10*self.mid+self.sid < 10*other.mid+other.sid
		else: 
			return self.time < other.time
	
	def __gt__(self,other):
		return self.time < other.time
		
	def __sub__(self,other):
		return self.time - other.time
