class netRequest:
	'Base class for a network request'

	def __init__(self, method = "GET", params = "", header = {"Content-type:": "application/x-www-form-urlencoded", "Accept": "text/plain"}, port = 80, proto = "http", apiVersion = 1):
		''
		self.method = method
		self.params = params
		self.header = header
		self.port = port
		self.proto = proto
		self.apiVersion = apiVersion
		# print "%s %s %s %s %s %s" % (self.method, self.params, self.header, self.port, self.proto, self.apiVersion)
		
	def doGet(self):
		''
		
	def doPost(self):
		''
	
	def doPut(self):
		''
	
	def doDelete(self):
		''
		
	def getAttribs(self):
		print "%s %s %s %s %s %s" % (self.method, self.params, self.header, self.port, self.proto, self.apiVersion)