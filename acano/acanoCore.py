class coreNode:
	'Base class for a core node'
	
	def __init__(self, id = 0, nodeAddress = "x.x.x.x", adminTCPport = 8443, apiVersion = 1, httpMode = "https"):
		self.id = id
		self.nodeAddress = nodeAddress
		self.adminTCPport = adminTCPport
		self.apiVersion = apiVersion
		self.httpMode = httpMode
		# print "Core Node init"
		
	def createSpace(self, id):
		'Place holder'
	
	def destroySpace(self, id):
		'Place holder'
		
	def getCoreDetails(self):
		print "%s %s %s %s %s" % (self.id, self.nodeAddress, self.adminTCPport, self.apiVersion, self.httpMode)
		