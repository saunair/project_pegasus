#include<iostream>
#include<queue>
#include<vector>

using namespace std;


vector<vector<int>>& example_1(){
    static vector<vector<int>> a = {
        {2,1,1},
        {1,1,0},
        {0,1,1}
    };
    return a;
}


vector<vector<int>>& example_2(){
    static vector<vector<int>> a = {
        {2,1,1},
        {0,1,1},
        {1,0,1}
    };
    return a;
}


int main(int argc, const char* argv[]){
    auto eg1 = example_1();
    return 0;
}
