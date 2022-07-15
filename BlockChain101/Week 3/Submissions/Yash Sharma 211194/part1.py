def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp

n = int(input("Enter n here:"))
p = 2
e = 2
while(n % p != 0):
   p = p + 1
q = n / p
phi = (p-1)*(q-1)
while (e < phi):
    if(gcd(e, phi) == 1):
        break
    else:
        e = e+1
print("e =",e)