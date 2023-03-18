import math
first=input("enter the first no.:")
c=input("enter the operator +-*%/:")
second=input("enter the second no.:")
first=int(first)
second=int(second)

if c=="+":
    print(first+second)
elif c=="-":
    print(first-second) 
elif c=="%":
    print(first%second) 
elif c=="*":
    print(first*second)
elif c=="/":
    print(first/second)
else:
    print( "invalid operatpr")