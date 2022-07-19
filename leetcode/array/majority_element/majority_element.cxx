#include<iostream>
#include<climits>
#include<vector>


using namespace std;

int majority_element(vector<int>& number_list){
    int count = 0;
    int maximum = INT_MIN;

    for(auto& number: number_list){
        if(maximum == number){
            count++;
        }
        else if(count == 0){
            maximum = number;
            count = 1;
        }
        else{
            count --;
        }
    }
    return maximum;
}


int main(int argc, const char* argv){
    vector<int> test_vector =  {2,2,1,1,1,1, 2,2, 2, 2, 3};
    cout<<"Majority element is: "<<majority_element(test_vector)<<endl;
    return 0;
}
