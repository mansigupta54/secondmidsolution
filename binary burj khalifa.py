a=int(input())
q=len(list("{0:b}".format(a)))
for i in range(0,a+1):
      w=len(list("{0:b}".format(i)))
      while w<q:
        print(" ",end="")
        w=w+1
      print(int("{0:b}".format(i)))
