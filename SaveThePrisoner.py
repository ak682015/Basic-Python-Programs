a = [5,2,2]
count=a[2]-1
for i in range(a[2],a[0]):
	if(a[1]==0):
		#count+=1
		break
	count+=1
	a[1]=a[1]-1
print(count)