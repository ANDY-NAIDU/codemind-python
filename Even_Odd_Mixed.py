a=int(input())
b=0
c=0
while a>0:
    temp=a//10
    a=a%10
    if a%2==0:
        b+=1
    else:
        c+=1
    a=temp
if b>0 and c==0:
    print('Even')
elif c>0 and b==0:
    print('Odd')
elif b>0 and c>0:
    print('Mixed')
    