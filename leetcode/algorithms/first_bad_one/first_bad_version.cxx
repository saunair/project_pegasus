#include<iostream>

using namespace std;


int first_bad_version(int n, int bad_version){
    bool is_bad;
    int start = 0;
    int end = n;
    int soln = -1;
    int mid = -1;
    int a;
    while(start<=end){ 
        mid = (start + end) / 2;
        cout<<"Explored "<<mid<<" "<<start<<" "<<end<<endl;
        cin>>a;
        is_bad = mid>=bad_version; // This is the hidden condition.
        if(is_bad){
           soln = mid;
           end = mid; 
           if (!((mid-1)>=bad_version)){
               return soln;
           }
        }
        else{
           start = mid +1; 
        }
    }
    return soln;
}


int main(int argc, const char* argv[]){
    cout<<first_bad_version(6, 2)<<endl;
    return 0;
}
