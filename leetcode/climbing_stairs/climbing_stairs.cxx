#include<iostream>
#include<vector>

using namespace std;


int num_of_ways(int stairs){
    vector<int> dp(stairs, 0);
    cout<<dp.size()<<"this"<<endl;
    dp[0] = 1;
    dp[1] = 2;
    for(int index=2; index<dp.size(); index++)
    {
        dp[index] = dp[index - 1] + dp[index - 2]; 
    } 
    return dp[stairs -1];
}


int main(int argc, const char* argv[]){
    const char* num_of_stairs = argv[1];
    int stairs = 0;
    int i = 0;
    char a;
    int string_len = sizeof(num_of_stairs) / sizeof(num_of_stairs[0]);
    while(num_of_stairs[i] != char(0)){
        stairs = stairs*10 + int(num_of_stairs[i] - '0');
        i++;
    }
    cout<<"Answer:"<<num_of_ways(stairs)<<endl;
    return 0;
}
