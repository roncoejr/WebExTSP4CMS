class space:
	'Base class for a space'
	
	def __init__(self, id, call, userUri, secondaryUri, callId, layout):
		self.id
		self.call = call
		self.userUri = userUri
		self.secondaryUri = secondaryUri
		self.callId = callId
		self.layout = layout
		
	def createCall(self, id, call):
		''
	
	def destroyCall(self, id):
		''
	
	def create(self, userUri, secondaryUri, callId, layout):
		''
	
	def destroy(self, id):
		''