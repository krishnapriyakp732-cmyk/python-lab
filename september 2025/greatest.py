a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if ((a>b) & (a>c)):
    print("greatest is",a)
elif ((b>a) & (b>c)):
    print("greatest is",b)
elif ((c>a) & (c>a)):
    print("greatest is",c)
else:
    print("plz leave me alone....")
