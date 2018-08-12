n = 7
scores = [100,100,50,40,40,20,10]
m = 4
alice = [5,25,50,120]

def countR(scores):
	

for i,v in enumerate(alice):
	scores.append(alice[i])
	scores.sort(reverse=True)
	print(scores.index(v)+1-countR(scores))
	print(scores)
