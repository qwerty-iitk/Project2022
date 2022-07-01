#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

int gcd(int a, int b) {
   if (b == 0)
   return a;
   return gcd(b, a % b);
}


bool check_prime(long long n) {
  bool is_prime = true;

  // 0 and 1 are not prime numbers
  if (n == 0 || n == 1) {
    is_prime = false;
  }

  for (long long i = 2; i <= n / 2; ++i) {
    if (n % i == 0) {
      is_prime = false;
      break;
    }
  }

  return is_prime;
}

int main(){

    long long n, d, p, q, e;
    cout<<"Enter private key n, d :-"<<endl;
    cin>>n>>d;
    for(p = 1; p < n; ++p){
        if(n%p==0 && check_prime(p)==true){
            q = n/p;
            break;
        }
    }
    //cout<<p<<q<<endl;
    //cout<<gcd(15,20);
    //now we have prime p,q with us.

    //calculating phi(n) :-
    long long phi = (p-1)*(q-1);
    int ans;
    //calculating e, given d :- we have to use the fact that ed = 1 mod phi ;
    for(long long e = 2; e < phi; ++e){
        if(gcd(e, phi)==1 && ( (e*d) % phi) == 1) {
            ans = e;
            break;
        }
    }
    //we have desired e, 1 < e < phi and gcd(e, phi) = 1, given a particular d.

    cout<<"Public key is {e, n} = {";
    cout<<ans<<", "<<n<<"}";
    



}