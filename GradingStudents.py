grades = [45, 67, 73, 72, 30, 38, 37, 79, 78, 80]
for j,i in enumerate(grades):
	if(i<38):
		continue
	if(i%5>=3):
			grades[j] = i+5-i%5
print(grades)