l = [[1,3,8],[2,4,5],[4,32,1]]
ans=0
Sans=0
j=0
for i in range(len(l)):
	ans+=l[i][i]
for i in range(len(l)-1,-1,-1):
	Sans+=l[i][j]
	j+=1
print(Sans)

