import math as mt

def gcd(a:int,b:int)->int:
    if(b>a):
        a,b=b,a
    while(True):
        t=a%b
        if t==0 :
            return b
        a,b=b,t

def iscomp (n:int)->bool:
    if(n<=1):
        return True
    for i in range(2,n):
        if(n%i==0):
            return True

    return False

def prime(n:int)->int:
    i=2
    while(i<n):
        if (not iscomp(i)) and (n%i==0):
            return i
        else:
            i+=1


n=int(input("Enter n: "))
d=int(input("Enter d : "))
msg=int(input("Enter the message: "))

p=prime(n)
q=n/p
phi =(p-1)*(q-1)
e=2

for e in range (2,int(phi)):
    if (gcd(e, phi)==1):
        break

k=((d*e)-1)/phi

c=pow(msg,e)
c=mt.fmod(c,n)

print("public Key : ",n,"\ne : ",e)
print("Encrypted msg : ",c)