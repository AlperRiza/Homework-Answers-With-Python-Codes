import time
x=int(input())
c=0
y=x
while y>=10:
    y=int(y/10)
    c=c+1
a=0
b=0
while b<=c:
    a=int(x/(10**b))%10
    b=b+1
    print(a)
time.sleep(3)    
