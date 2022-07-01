#include <iostream>
using namespace std;

int main() {
	// your code goes here

int n,d,e;
cin>>n>>d;
int i=2;
while(n%i!=0){
    i++;
}
int t=n/i;
int a=(i-1)*(t-1);
//printf("%d, %d\n", i,t);
int k=0;
while(((k*a)+1)%d!=0){
    k++;
}
//printf("%d\n", k);
e=((k*a)+1)/d;
cout<<e<<", "<<n;

	return 0;
}
