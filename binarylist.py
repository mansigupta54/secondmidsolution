def flt(i):
	if i==0 or i==1:
		return True
	else:
		return False
a=[1,0,0,1,2,3,4,5,7,6,7]
a=filter(flt,a)
print(a)
a=list(map(str,a))
s=''.join(a)
print(int(s,2))

