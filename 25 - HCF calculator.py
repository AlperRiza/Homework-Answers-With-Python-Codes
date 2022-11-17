import time
a=int(input())
b=int(input())
c=a
while c != 1:
    if a%c==0:
        if b%c==0:
            print(c)
            c=1
        else:
            c=c-1
    else:
        c=c-1
time.sleep(3)
