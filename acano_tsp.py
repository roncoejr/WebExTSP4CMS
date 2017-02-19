import acano_tspWorker

def main():
	print "Ready to rock!"
	myNode = acano_tspWorker.acano_tspWk()
	myNode.mNode.getCoreDetails()
	myNode.nReq.getAttribs()
	
	content = dir()
	print("%s" % content)
	
main()