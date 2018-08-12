s=7
t=11
a=5
b=15
apples=[-2,2,1]
oranges=[5,-6]
coapple=0
coorange=0
for i in range(len(apples)):
	if((a+apples[i]) in range(s,t+1)):
		coapple+=1
for i in range(len(oranges)):
	if((b+oranges[i]) in range(s,t+1)):
		coorange+=1
print(coapple,coorange)
