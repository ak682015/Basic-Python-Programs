ar = [1,3,2,6,1,2]
count=0
for i in range(len(ar)):
		for j in range(len(ar)):
			if(i==j):
				break
			else:
				if((ar[i]+ar[j])%3==0):
					count+=1

print(count)