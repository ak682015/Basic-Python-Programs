def almostIncreasingSequence(sequence):
	b = False
	for i in range(len(sequence)):
		s =set(sequence)
		temp=sequence[i]
		del(sequence[i])
		if(sequence.count(temp)>1 or len(s)<len(sequence)):
			b=False
			return b
		if(sequence==sorted(sequence)):
			b=True
		sequence.insert(i,temp)
	return b
print(almostIncreasingSequence([1, 2, 1, 2]))
