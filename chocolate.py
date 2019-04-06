a=int(input('TOTAL WEIGHT'))
b=int(input('CHOCOLATE OF 5Kg'))
c=int(input('CHOCOLATE OF 1Kg'))
n=a*5+c*1
if (n>a):
	print('TRUE,OVERFLOW')
	if(b==1):
		print('5kg used',a)
		print('1kg used',a-(b*5))

elif(n<a):
	print('FALSE,OVERFLOW')
elif(n==a):
	print('TRUE, ENOUGH')
