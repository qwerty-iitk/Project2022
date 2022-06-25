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
k=(d*e-1)/phi
str=input('message=\n')
i=0
list=[]
for x in str:
    list.extend(x)
for x in list:
    if ord(x)<=57 and ord(x)>=48:
        list[i]=int(x)
        i=i+1
    else:
        list[i]=ord(x)-64
        i+=1   
print(list)
i=0
for x in list:
    if int(x/10)==0:
        i+=1
    if int(x/10)>0:
        i+=2
sum=0
b=i
for x in list:
    if int(x/10)==0:
        temp=x
        for h in range(1,b):
            temp=temp*10
        sum=sum+temp
        b=b-1
    else:
        temp=int(x/10)
        for h in range(1,b):
            temp=temp*10
        sum=sum+temp
        b=b-1
        temp=x%10
        for h in range(1,b):
            temp=temp*10
        sum=sum+temp
        b=b-1
rem=(math.pow(sum,e))%n
print('Public key=(',e,',',n,')')
print('Encrypted Message=',int(rem))


        
                





