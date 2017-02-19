from acano import *

class acano_tspWk():
	'Base class for the TSP worker'
	def __init__(self):
		self.mNode = acanoCore.coreNode(httpMode = "httpBULL")
		self.nReq = networkRequest.netRequest()
	
