#include<iostream>
#include<math.h>
#include "bits/stdc++.h"

using namespace std;


int gcd(int a, int b)
{
    int t;
    if(b>a) 
    {
        int c=a;
        a=b;
        b=c;
    }
    while(1)
    {
        t=a%b;
        if(t==0) return b;
        else
        {
            a=b;
            b=t;
        }
    }
}

bool isprime(int n)
{
    if(n<=1) return false;

    for(int i=2;i<n;i++)
    {
        if(n%i==0) return false;
    }

    return true;
}

int prime(int n)
{
    for(int i=2;i<=n;i++)
    {
        if(isprime(i) && n%i==0) return i;
    }
}


int main()
{
    
    int n,d;
    cin>>n>>d;

    int p=prime(n);
    int q=n/p;
    int phi=(p-1)*(q-1);
    int e=2;
    
    while (e < phi)
    {
        if (gcd(e, phi)==1)
            break;
        else
            e++;
    }

    
    int k=((d*e)-1)/phi;

    cout<<"public key :\nn : "<<n<<"\ne :"<<e<<endl;
	return 0;
}
