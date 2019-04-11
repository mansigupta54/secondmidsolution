a=set()
b=set()
for i in range(1,21):
	c=0
	for j in range(1,i+1):
		if i%j==0:
			c=c+1
	if c==2:
		a.add(i)
for i in range(1,21):
	if i%2==1:
		b.add(i)
print(a)
print(b)
print("Unoin is",a.union(b))
print("Intersection is",a.intersection(b))
print("Difference is ",a-b)
