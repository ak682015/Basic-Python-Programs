score = [10,5,20,20,4,5,2,25,1]
max,min = score[0],score[0]
count_max,count_min=0,0

for i in score:
	if(i>max):
		max=i
		count_max+=1
	if(i<min):
		min=i
		count_min+=1

print(count_max,count_min)