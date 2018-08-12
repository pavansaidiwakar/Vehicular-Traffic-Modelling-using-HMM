from hmm import Model
from hmm import train
from PIL import Image



x=[20,95,195,296,320,373,529,561,608,681,727,763,800,861,887,1175,1201,1221,1246,1281]
y=[597,590,571,546,538,521,470,459,444,422,411,402,393,378,372,266,256,249,240,227]

#OBSERVED_STATE=['','','']
OBSERVED_STATE=['']*119	
HIDDEN_STATE=['']*119
ssno=0
pixsum=[0]*119
for j in range(0,119):
	filename='/home/nisarg/PythonHMM/Screenshots/1/'
	ssno=ssno+1
	filename=filename+str(ssno)	
	im = Image.open(filename) #Can be many different formats.
	pix = im.load()
	
	#SEG1
	for i in range(0,5):
		P = pix[x[i],y[i]]
		B = sum(P)
		pixsum[j]=pixsum[j]+B
		M=[0,0,0,0]
		#print B
		#print P #Get the RGBA Value of the a pixel of an image
		if B in range(180,215):
			M[0]=M[0]+1
		elif B in range(215,270):
			M[1]=M[1]+1
		elif P[0]>200:
			M[2]=M[2]+1
		else:
			M[3]=M[3]+1
		a=max(M[0],M[1],M[2],M[3])
	if a==M[0]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'M'
	elif a==M[1]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'R'
	elif a==M[2]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'O'
	elif a==M[3]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'G'
	
	#SEG2
	for i in range(5,10):
		P = pix[x[i],y[i]]
		B = sum(P)
		M=[0,0,0,0]
		pixsum[j]=pixsum[j]+B
		#print B
		#print P #Get the RGBA Value of the a pixel of an image
		if B in range(180,215):
			M[0]=M[0]+1
		elif B in range(215,270):
			M[1]=M[1]+1
		elif P[0]>200:
			M[2]=M[2]+1
		else:
			M[3]=M[3]+1
		a=max(M[0],M[1],M[2],M[3])
	if a==M[0]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'M'
	elif a==M[1]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'R'
	elif a==M[2]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'O'
	elif a==M[3]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'G'
	#SEG3
	for i in range(10,15):
		P = pix[x[i],y[i]]
		B = sum(P)
		M=[0,0,0,0]
		pixsum[j]=pixsum[j]+B
		#print B
		#print P #Get the RGBA Value of the a pixel of an image
		if B in range(180,215):
			M[0]=M[0]+1
		elif B in range(215,270):
			M[1]=M[1]+1
		elif P[0]>200:
			M[2]=M[2]+1
		else:
			M[3]=M[3]+1	
		a=max(M[0],M[1],M[2],M[3])
	if a==M[0]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'M'
	elif a==M[1]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'R'
	elif a==M[2]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'O'
	elif a==M[3]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'G'
	#SEG4
	for i in range(15,20):
		P = pix[x[i],y[i]]
		B = sum(P)
		M=[0,0,0,0]
		pixsum[j]=pixsum[j]+B
		#print B
		#print P #Get the RGBA Value of the a pixel of an image
		if B in range(180,215):
			M[0]=M[0]+1
		elif B in range(215,270):
			M[1]=M[1]+1
		elif P[0]>200:
			M[2]=M[2]+1
		else:
			M[3]=M[3]+1
		a=max(M[0],M[1],M[2],M[3])
	if a==M[0]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'M'
	elif a==M[1]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'R'
	elif a==M[2]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'O'
	elif a==M[3]:
		OBSERVED_STATE[j]=OBSERVED_STATE[j]+'G'
		

print OBSERVED_STATE

for i in range(0,119):
	if pixsum[i]>7500:
		HIDDEN_STATE[i]="OPEN"
	elif pixsum[i]>6600:
		HIDDEN_STATE[i]="MILDLY CONGESTED"
	elif pixsum[i]>5545:
		HIDDEN_STATE[i]="MODERATELY CONGESTED"
	else:
		HIDDEN_STATE[i]="HEAVILY CONGESTED"
	print HIDDEN_STATE[i]
	

 
sequence = [(HIDDEN_STATE,OBSERVED_STATE)]

for i in range(5):
	print '_'*80

print ''*80

print "THE HIDDEN STATE AND OBSERVED STATE PREDICTED FOR THE NEXT TIME INTERVAL IS\n"

train(sequence)

	


