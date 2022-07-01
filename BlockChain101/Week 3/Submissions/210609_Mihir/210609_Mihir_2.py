import math

n=int(input("Enter the value of n : "))
d=int(input("Enter the value of d: "))
def check_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return -1
    return 1
def hcfnaive(a, b):
    if(b == 0):
        return abs(a)
    else:
        return hcfnaive(b, a % b)
for i in range(2,n):
    if n%i==0 and check_prime(i)==1:
        p=i
        break
q=int(n/p)
phi=(p-1)*(q-1)
e=2
for f in range (2, phi):
    if(hcfnaive(f, phi) == 1 & (d*f)%phi==1):
        e = f
        break
    else:
        f += 1
print("(e,n)=(",e,",",n,")")

#encrypting the message
message =input("Enter the message : ")
#associating every letter with its alphabetic number using ascii codes :-
def to_ascii(text):
    ascii_values = [(ord(character)-64) for character in text]
    return ascii_values
ascii_array=to_ascii(message)
ans_str = ""
length=len(ascii_array)
for i in range(1,length+1):
    curr_str=str(ascii_array[i-1])
    ans_str += curr_str
cipher=int(ans_str)
c=math.pow(cipher, e)%n
print(c)