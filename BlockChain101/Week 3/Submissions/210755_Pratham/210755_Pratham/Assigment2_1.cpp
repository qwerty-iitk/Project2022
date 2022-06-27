
#include<iostream>
using namespace std;

int gcd_(int a, int b){
    int result=min(a,b); // Find Minimum of a nd b
    while(result>0)
    {
        if(a%result==0 && b%result==0)
        {
            break;
        }
        result--;
    }
    return result;
}
int main(){
    int d,n;
    cout<<"Enter n of private key"<<endl;
    cin>>n;
    cout<<"Enter d of private key"<<endl;
    cin>>d;

    int p;
    int q;
    for(int i=2;i<n;i++){
        if(n%i==0){
            p=i;
            q=n/p;
            break;
        }
    }

    int e=0;
    int x=(p-1)*(q-1);
    for(int j=2;j<(p-1)*(q-1);j++)
    {
        if(gcd_(j,x)==1 and n%j!=0){
            e=j;
            break;
        }

    }

    cout<<"The public key is ("<<n<<","<<e<<")";

    

}