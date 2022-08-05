import Crypto
import math
from Crypto.PublicKey import RSA


n=input('input n of private key \n')
d=input('input d of private key\n')


i=2

while i < n:
    if n%i==0:
        p=i
        q=n/p
        break
    i=i+1
    


e=0
x=(p-1)*(q-1)

for j in range(x):
    if math.gcd(j,x)==1 and n%j!=0:
        e=j
        break


key=Crypto.PublicKey.RSA.construct((n,e,d))

publickey=key.publickey()
msg=input('Input message to be encrypted')
encrypted = publickey.encrypt(msg)

print('encrypted message:', encrypted)
print('public key:', publickey)