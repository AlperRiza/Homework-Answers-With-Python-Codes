import time
a="1"
x=int(input())
while x>1:
    b=x%2
    x=int(x/2)
    if b==0:
        a=a+"0"
    else:
        a=a+"1"
print(a)
time.sleep(3)

