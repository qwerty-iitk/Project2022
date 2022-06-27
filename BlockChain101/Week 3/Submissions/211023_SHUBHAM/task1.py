import math
def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp
  
n=input("Enter vaue of n:\n")
d=input("Enter value of d:\n")
n=int(n)
d=int(d)
nsqrt=math.sqrt(n)
nsqrt=int(nsqrt)
p=2
for p in range(2,nsqrt):
    if n%p==0:
        break
q=n/p
q=int(q)
# print(p,q)
phi=(p-1)*(q-1)
e=2
if p-1>q-1:
    c=q-1
else:
    c=p-1
for e in range(2,c):
    if gcd(e,phi)==1:
        break
#print(e)
print("PUBLIC KEY=",n, ',' ,e)

