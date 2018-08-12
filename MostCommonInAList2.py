def comlist(list): 
	list2,list3=[],[]
	for i in list:
		if( i not in list2):
			list3+=[i]
		list2+=[i]
	count=0
	for i in list3:
		if(list2.count(i)>count):
			count=list2.count(i)
			no=i
	print("MAX=",no)

if __name__ == '__main__':
	l1 = [1,2,3,4,5,3,3]
	l2 = [1,2,3,4,5,3]
	comlist(l1+l2)