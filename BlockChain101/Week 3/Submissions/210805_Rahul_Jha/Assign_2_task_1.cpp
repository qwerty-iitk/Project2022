#include<iostream>
#include<math.h>
#include "bits/stdc++.h"

using namespace std;

#define MAXN 100001

// stores smallest prime factor for every number
int spf[MAXN];

// Calculating SPF (Smallest Prime Factor) for every
// number till MAXN.
// Time Complexity : O(nloglogn)
void sieve()
{
	spf[1] = 1;
	for (int i=2; i<MAXN; i++)

		// marking smallest prime factor for every
		// number to be itself.
		spf[i] = i;

	// separately marking spf for every even
	// number as 2
	for (int i=4; i<MAXN; i+=2)
		spf[i] = 2;

	for (int i=3; i*i<MAXN; i++)
	{
		// checking if i is prime
		if (spf[i] == i)
		{
			// marking SPF for all numbers divisible by i
			for (int j=i*i; j<MAXN; j+=i)

				// marking spf[j] if it is not
				// previously marked
				if (spf[j]==j)
					spf[j] = i;
		}
	}
}

// A O(log n) function returning primefactorization
// by dividing by smallest prime factor at every step
vector<int> getFactorization(int x)
{
	vector<int> ret;
	while (x != 1)
	{
		ret.push_back(spf[x]);
		x = x / spf[x];
	}
	return ret;
}

// Function to find out GCD
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

// driver program for above function
int main()
{
	// precalculating Smallest Prime Factor
	sieve();
    // Taking Private Key input
    int n,d;
    cin>>n>>d;

	// calling getFactorization function
	vector <int> fac = getFactorization(n);

    // Calculating P,Q,Phi

    int p=fac[fac.size()-1];
    int q=n/p;
    int phi=(p-1)*(q-1);
    int e=2;
    // Finding Appropriate e
    while (e < phi)
    {
        // e must be co-prime to phi and
        // smaller than phi.
        if (gcd(e, phi)==1)
            break;
        else
            e++;
    }

    //Finding the Constant k
    int k=((d*e)-1)/phi;

    cout<<"public key :\nn : "<<n<<"\ne :"<<e<<endl;

	return 0;
}
