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


msg =input("Enter msg=")
#converting into string as shown in gfg doc with the help of internet
def to_ascii(text):
    ascii_values = [(ord(character)-64) for character in text]
    return ascii_values
ascii_values=to_ascii(msg)
cd=""
j=len(ascii_values)
for i in range(1,j+1):
    ab=str(ascii_values[i-1])
    cd=cd+ab
m=int(cd)
c=(m**e)%n
print("Encypted message=",c)

    




    
