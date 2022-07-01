#include<iostream>
#include<math.h>
using namespace std;
bool isnatural(float k)
{
  int x=k;
  if(k-x==0)return 1;
  return 0;  
}
int main()
{
 int n;
 float d;
 cin>>n>>d;
 int i;
 for(i=2; i<n; i++)
 {
    if(n%i==0)break;
 }
 float l=n; float p=i; 
 float j=n/i;
 for(int k=1;; k++)
 {
    float num=(k*(p-1)*(j-1) +1 )/d;
    if(isnatural(num)){
        cout<<num<<" "<<n;
        break;
    }
 }
    return 0;
}