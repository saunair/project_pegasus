
#include<iostream>

using namespace std;

void test_memory_expermient(){
    int a[5] = {0, 1, 2, 3, 4};
    int b[10] = {0, 1, 2, 3, 4, 0, 1, 2, 3, 4};
    int i = 0;
    for(int k=0; k<10; k++){
       a[k] = k;
    }
}



int main(int argc, const char* argv[]){
    test_memory_expermient();
    return 0;
}
