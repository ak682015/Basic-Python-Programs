arr = [1,3,4,-4,2,-3,2,-5,-4,0,0,0]
plus,minus,zero=0,0,0
for i in arr:
	if(i>0):
		plus+=1
	if(i<0):
		minus+=1
	if(i==0):
		zero+=1
print(plus/len(arr))
print(minus/len(arr))
print(zero/len(arr))