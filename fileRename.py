import os

for dpath, dnames, fnames in os.walk('	'):
	for f in fnames:
		os.chdir(dpath)
		#print(f)
		g="1_"+f
		#print(g)
		os.rename(f, g.replace(' ','_'))