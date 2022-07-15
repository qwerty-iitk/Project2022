import math
n=int(input('n=\n'))
d=int(input('d=\n'))
c=math.sqrt(n)
p=2
for p in range(2,int(c)):
    if n%p==0:
        break
q=n/p
phi=int((p-1)*(q-1))
e=2
for e in range(2,int(p)):
    if math.gcd(phi,e)==1:
        break
print('Public key=(',e,',',n,')')
