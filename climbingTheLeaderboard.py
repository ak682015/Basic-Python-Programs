n = 7
scores = [100,100,50,40,40,20,10]
m = 4
alice = [5,25,50,120]
a=[]

for i,j in enumerate(alice):
	scores.append(j)
	b=(list(set(scores)))
	b.sort(reverse=True)
	a+=[b.index(j)+1]

print(a)