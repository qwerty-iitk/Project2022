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

bool iscomp(int n)
{
    if(n<=1) return true;

    for(int i=2;i<n;i++)
    {
        if(n%i==0) return true;
    }

    return false;
}

int prime(int n)
{
    for(int i=2;i<=n;i++)
    {
        if(!iscomp(i) && n%i==0) return i;
    }
}


int main()
{
    int n,d;
    cin>>n>>d;

    int p=prime(n),q=n/p,phi=(p-1)*(q-1),e;

    for(e=2;e<phi;e++)
    {
        if(gcd(e,phi)==1) break;
    }
   
    int k=((d*e)-1)/phi;

    cout<<"public key (n,e) : \n"<<n<<" "<<e<<endl;
	return 0;
}