from math import sqrt
a,b,c=map(int,input().split())
s=(a+b+c)/2
e=(sqrt(s*(s-a)*(s-b)*(s-c)))
rounded = "{:.2f}".format(e)
print(rounded)