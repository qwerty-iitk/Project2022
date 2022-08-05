import math
 
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))
 
n = p * q

r= (p-1)*(q-1)
 
def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e
 
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            r=e
            e=b
 
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        return(gcd,t,s)
 
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        return s%r
 
for i in range(1,1000):
    if(egcd(i,r)==1):
        e=i

eugcd(e,r)
d = mult_inv(e,r)
public = (e,n)
private = (d,n)
print("Public Key is:",public)

def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    w=0
    for i in n_text:
        if(i.isupper()):
            w = ord(i)-65
            c=(w**e)%n
            x.append(c)
        elif(i.islower()):               
            w= ord(i)-97
            c=(w**e)%n
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    return x
 
message = input("What would you like encrypted?:")
 
enc_msg=encrypt(public,message)
print("Your encrypted message is:",enc_msg)
