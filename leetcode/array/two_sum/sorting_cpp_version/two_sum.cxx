#include <iostream>
#include <algorithm>
#include <vector>
#include "two_sum.h"


using namespace std; 


vector<uint> two_sum(vector<uint> input_array, uint required_sum){
    sort(input_array.begin(), input_array.end());
    vector<uint>::iterator it1 = input_array.begin();
    vector<uint>::iterator it2 = prev(input_array.end());
    uint sum;
    while(it1<it2){
	sum= *it1 + *it2;
        if(sum < required_sum){
	    it1 = next(it1);
	}
	else if(sum > required_sum){
	    it2 = prev(it2);
	}
	else{
            return vector<uint> {*it1, *it2};
	}
    }
    return vector<uint> {};
}


vector<uint> three_sum(vector<uint> input_array, uint required_sum){
    sort(input_array.begin(), input_array.end());
    auto it0 = input_array.begin();
    while(it0 < input_array.end()){
	    uint current_required_sum = required_sum - *it0;
	    vector<uint>::iterator it1 = next(it0);
	    vector<uint>::iterator it2 = prev(input_array.end());
	    uint sum;
	    while(it1<it2){
		sum = *it1 + *it2;
		cout<<sum<<"\t"<<*it1<<"\t"<<*it2<<"\t"<<current_required_sum<<endl;
		if(sum < current_required_sum){
		    it1 = next(it1);
		}
		else if(sum > current_required_sum){
		    it2 = prev(it2);
		}
		else{
		    return vector<uint> {*it0, *it1, *it2};
		}
	    }
	    it0=next(it0);
    }
    return vector<uint> {};
}


int main(int argc, const char* argv[]){
    vector<uint> input_array = {111, 2, 10, 0};
    if(argc<1){
	cout<<"Please enter valid inputs. The sum and the array respectively"<<endl;
	return 0;
    }
    uint sum_reqd = uint(*argv[0]); // Remember only single digits would work here!
    vector<uint> solution = two_sum(input_array, 12);
    if(solution.size() == 0){
        cout<<"No solutions found"<<endl;
    }
    else{
	    cout<<"The solution is:"<<solution[0]<<"\t"<<solution[1]<<endl;
    }
    vector<uint> solution_3 = three_sum(input_array, 124);
    if(solution_3.size() == 0){
        cout<<"No solutions found for three-sum"<<endl;
    }
    else{
	    cout<<"The solution is:"<<solution_3[0]<<"\t"<<solution_3[1]<<"\t"<<solution_3[2]<<endl;
    }
    return 1;
}
