def sort(a,key):
	
	for i in range(key,len(a)-1):
		a[i],a[i+1]=a[i+1],a[i]
	
	for i in range(len(a)-2):
		for j in range(len(a)-i-2):
			if(a[j] > a[j+1]):
				a[j], a[j+1] = a[j+1], a[j]

	for i in range(len(a)-1,key,-1):
		a[i],a[i-1]=a[i-1],a[i]

a = [4,856,478,1,65,85,78,21,69,31,658,96,6]
sort(a,2)
print(a)
