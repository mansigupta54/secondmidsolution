for j in range(100,1000):
	t=j
	sum=0
	while (j!=0):
		r=j%10
		sum=sum+(r*r*r)
		j=j/10
	if (sum==t):
		print(sum)
	
