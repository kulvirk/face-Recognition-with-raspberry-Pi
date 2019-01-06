import os
datasaved={'':500,'person1':100,'person2':200,'person3':300}

def validation(number):
	for key,val in datasaved.items():
 		if (key==number):
			if(val>100):
				print "open"
				break
		else:
			print "pay"
	return val
