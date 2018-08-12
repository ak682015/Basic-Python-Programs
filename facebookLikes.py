listname=[]
while True:
	name = input('Enter The name Of Friends:')
	if(name==""):
		break
	listname+=[name]
if(len(listname)>2):
	print(listname[0],",",listname[1]," and ",len(listname)-2,"others like your post")
elif(len(listname)==1):
	print(listname[0],"likes your post")
elif(len(listname)==2):
	print(listname[0],"and",listname[1],"likes your post")
