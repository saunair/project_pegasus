#include<iostream>
#include<vector>

using namespace std;


int num_of_paths(int rows, int columns){
    vector<vector<int>> dp(rows, vector<int>(columns));
    // The first row and column elements only have one way to reach them - going through the same action.
    for(int i=0; i<rows; i++){
        dp[i][0] = 1;
    }
    for(int i=0; i<columns; i++){
        dp[0][i] = 1;
    }
    // Now paths to remaining elements can be filled column wise, 
    for(int i=1; i<rows; i++){
        for(int j=1; j<columns; j++){
            dp[i][j] = dp[i-1][j] + dp[i][j - 1];
        }
    }
    return dp[rows-1][columns-1];
}


int main(int argc, const char* argv[]){
    int rows = 3;
    int columns = 2;
    cout<<"The number of paths are:"<<num_of_paths(rows, columns)<<endl;
    return 0;
}
