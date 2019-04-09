h=open('mansi.txt','w')
while True:
                s=input("sign(+,-,*,/):")
                if s=='0':break
                if s in ('+','-','*','/'):
                                x=float(input("x="))
                                y=float(input("y="))
                                if s=='+':
                                                h.write("x")
                                                h.write("%.2f"%(x+y))
                                elif s=='-':
                                                h.write("%.2f"%(x-y))
                                elif s=='*':
                                                h.write("%.2f"%(x*y))
                                elif s=='/':
                                                      if y!=0:
                                                                h.write("%.2f"%(x/y))
                                                      else:
                                                                h.write("division by zero!")
                else:
                                                                      h.write("Invalid operation")
                h.close()



