s = "07:23:45PM"

if 'P' in s:
	temp=s[2:-2]
	ss=str(int(s[:2])+12)
	new=ss+temp
else:
	temp=s[:-2]
