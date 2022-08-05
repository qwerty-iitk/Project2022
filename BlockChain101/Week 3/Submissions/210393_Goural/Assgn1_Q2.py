# cook your code here
import math
n=int(input())
d=int(input())
i=2
while(n%i!=0):
    i=i+1
t=n/i
a=(i-1)*(t-1)
k=0
while(((k*a)+1)%d!=0):
    k=k+1
    
e=int(((k*a)+1)/d)
s1 = "(e,n)=("
s2 = ","
s3 = ")"
print(s1 ,e,s2,n,s3)
msg =input()
def to_ascii(text):
    ascii_values = [(ord(character) - 64) for character in text]
    return ascii_values
g=to_ascii(msg)

def convert(list):
      
    # Converting integer list to string list
    s = [str(i) for i in list]
      
    # Join list items using join()
    res = int("".join(s))
      
    return(res)
b= convert(g)
c=int(b)

#print(c**e)
f=(c**e)%n
print("Encypted message=",f)
