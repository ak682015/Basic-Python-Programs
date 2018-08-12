input =' I said "Indeed, we HAVE to return", HE exclaimed, "I WONT" A Quotation THE "repetition" one "EXPRESSION" as part OF another ONE '
quotes,caps="",""
j,k,m=0,0,0
while(m<len(input) or j<len(input)):

	if(input[m].isupper() and input[m+1].isupper()):
		caps+=' '
		while True:
			caps+=input[m]
			m+=1
			if(not input[m].isupper()):
				break

	if(j<len(input)):
		if(input[j]=='"'):
			k=j
			quotes+=" "
			while(input[k+1]!='"'):
				quotes+=input[k]
				k+=1
			j=k+1
			quotes+=input[k];quotes+=input[k+1]

	j+=1;m+=1

print('Input=',input)
print('Quotes=',quotes)
print('caps=',caps)