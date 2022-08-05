import math as mt
 
MAXN = 100001
 
# stores smallest prime factor for
# every number
spf = [0 for i in range(MAXN)]
 
# Calculating SPF (Smallest Prime Factor)
# for every number till MAXN.
# Time Complexity : O(nloglogn)
def sieve():
    spf[1] = 1
    for i in range(2, MAXN):
         
        # marking smallest prime factor
        # for every number to be itself.
        spf[i] = i
 
    # separately marking spf for
    # every even number as 2
    for i in range(4, MAXN, 2):
        spf[i] = 2
 
    for i in range(3, mt.ceil(mt.sqrt(MAXN))):
         
        # checking if i is prime
        if (spf[i] == i):
             
            # marking SPF for all numbers
            # divisible by i
            for j in range(i * i, MAXN, i):
                 
                # marking spf[j] if it is
                # not previously marked
                if (spf[j] == j):
                    spf[j] = i
 
# A O(log n) function returning prime
# factorization by dividing by smallest
# prime factor at every step
def getFactorization(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]
 
    return ret

# Function to calculate gcd
def gcd(a:int,b:int)->int:
    if(b>a):
        a,b=b,a
    while(True):
        t=a%b
        if t==0 :
            return b
        a,b=b,t
 
# Driver code
 
#taking input
n=int(input("Enter n: "))
d=int(input("Enter d : "))
msg=int(input("Enter the message: "))

# precalculating Smallest Prime Factor
sieve()
# calling getFactorization function
fac = getFactorization(n)

#Calculating P,Q & Phi
p=fac[len(fac)-1]
q=n/p
phi =(p-1)*(q-1)

#Calculating e
e=2
while (e < phi):
    if (gcd(e, phi)==1):
        break
    else:
        e+=1

k=((d*e)-1)/phi

#Encrypt Mssg
c=pow(msg,e)
c=mt.fmod(c,n)

print("public Key : \nn:{}\ne: {}".format(n,e))
print("Encrypted msg : ",c)