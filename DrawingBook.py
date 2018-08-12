def solve(n, p):
	if(n//2>p):
		return p//2
	else:
		if(p==n-1):
			return 0
		return p//2

print(solve(6,2))