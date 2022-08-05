import math

n=input("input n:")
e=input("input e:")

n=int(n)
e=int(e)
i=2
d=""
N=1
x=n
while(n>=i):
    k=1
    t=0
    j=0
    if(n%i==0):
        N=n
        while(n%i==0):
            k=k*i
            n=n/i
        while(k<10**(e-1)):
            k=k*10
            t=t+1
            j=j+1
        while(t>0):
            k=k//10
            t=t-1
        k=str(k)
        while(j!=0):
            k="0"+k
            j=j-1
    if(N%i==0):
        d=d+k
        N=1
    i=i+1
d=int(d)    
print((x,d))
