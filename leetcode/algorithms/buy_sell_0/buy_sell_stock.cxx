#include<iostream>
#include<vector>
#include<cctype>
#include<climits>


using namespace std; 


int maximim_profit(vector<int>& sequence){
    int minimum_stock_yet = INT_MAX;
    int maximum_profit = INT_MIN;
    for(auto& stock_price:sequence){
        maximum_profit = max(maximum_profit, stock_price - minimum_stock_yet);
        minimum_stock_yet = min(minimum_stock_yet, stock_price);
    }
    return maximum_profit;
}


int main(int argc, const char* argv[]){
    vector<int> first_test = {7,1,5,3,6,4};
    cout<<"Maximum profit is: "<<maximim_profit(first_test)<<endl;
    return 0;
}
