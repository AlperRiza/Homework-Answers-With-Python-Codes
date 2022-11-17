import time
x=int(input())
c=0
y=x
a=0
b=0
while y>=10:
    y=int(y/10)
    c=c+1
e=c
while b<=c:
    a=a+10**e*int((x/10**b)%10)
    b=b+1
    e=e-1
if x==a:
    print("palindrome")
else:
    print("not palindrome")
time.sleep(3)
