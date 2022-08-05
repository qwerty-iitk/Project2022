import math
n=int(input("Enter n: "))
d=int(input("Enter d: "))
def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp
def isprime(num):
    a=2
    while a<=math.sqrt(num):
        if num%a<1:
            return False
        a=a+1
    return num>1
for i in range(1,n):
    if n%i==0 and isprime(i):
        p=i
        break
q=int(n/p)
phi=(p-1)*(q-1)
e=2
while (e < phi):
    if(gcd(e, phi) == 1&(d*e)%phi==1):
        break
    else:
        e = e+1
print("(e,n)=(",e,",",n,")")

    




    
