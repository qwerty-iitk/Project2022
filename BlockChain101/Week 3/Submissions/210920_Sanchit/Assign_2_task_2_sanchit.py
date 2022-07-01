import math

def gcd(a:int,b:int)->int:
    if(b>a):
        a,b=b,a
    while(True):
        t=a%b
        if t==0 :
            return b
        a,b=b,t

def isprime (n:int)->bool:
    if(n<=1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False

    return True

def prime(n:int)->int:
    for i in range(2,n+1):
        if isprime(i) and (n%i==0):
            return i

n=int(input("Enter n: "))
d=int(input("Enter d : "))
msg=int(input("Enter the message: "))
p=prime(n)
q=n/p
phi =(p-1)*(q-1)
e=2

while (e < phi):
    if (gcd(e, phi)==1):
        break
    else:
        e+=1

k=((d*e)-1)/phi

#Encrypt Mssg
c=pow(msg,e)
c=math.fmod(c,n)

print("public Key : ",n,"\ne : ",e)
print("Encrypted msg : ",c)