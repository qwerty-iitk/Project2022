print("enter private key(n,d)")
n=int(input("Enter n :"))
d=int(input("enter d :"))

def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp
p=11
q=11
for i in range(2,n):
    if(gcd(i,1)==1 and gcd(n/i,1)==1 and n%i==0):
        p=i
        q=n/i
        break

t =int((p-1)*(q-1))

e=1;
for i in range(1,t):
    if(n%i!=0 and (d*i)%t==1):
        e=i
        break
print("public key(e,n) is (",e,",",n,")")
