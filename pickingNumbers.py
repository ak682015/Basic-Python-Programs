import time

t0=time.time()

a=[1,2,1,4,2,3,6,4,1,5,2,24,4,2,6]
print('ip:', a)
op=[]
a.sort()
print('sorted list:',a)
count=0
temp=[]

for index, current in enumerate(a):
	if(index==len(a)-1):
		break
	if(a[index]==a[index+1]-1):
		temp=(a[index],a[index+1])
		op+=[temp]
		count+=1
	else:
		pass

sum=[]
print('output:', op)

for value in op:
	temp=((a.count(value[0])+a.count(value[1])))
	#print('temp',temp)
	sum+=[temp]
ind=sum.index(max(sum))
print(ind)

fop=[]
print('sum',sum)


#print('op[ind]',op)

for i in op[ind]:
	s=a.count(i)
	fop+=map(int, str(i)*s)

print('final op:' ,fop)
print('length of op:',len(fop)) 



t1=time.time()
print("Time Elapse:",(t1-t0))
 ;.

	


	