import time
def pattern(n):
	for i in range(n,0,-1):
		for j in range(n,i,-1):
			print(" ",end="")
		a=ord('A')
		for k in range(0,i):
			print(chr(a)+"",end="")
			a=ord(chr(a))+1
		a=ord(chr(a))-1
		for l in range(i-1,0,-1):
			a=ord(chr(a))-1
			print(chr(a)+"",end="")
		print("")

t0=time.time()
print(pattern(50000))
t1=time.time()
print("Time Elapse:",(t1-t0))
