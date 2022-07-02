#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


vector<uint> unsorted_list = {2, 3, 70, 5, 9};


vector<uint> two_sum_hash(vector<uint>& v, uint sum) {
    vector<uint> set_hash; 
    vector<uint>::iterator it = v.begin();
    for(vector<uint>::iterator it = v.begin(); it!=v.end(); it++) {
	    uint sum_needed = sum - *it;
	    if (find(set_hash.begin(), set_hash.end(), sum_needed) != set_hash.end()){
		    return vector<uint> {*it, sum_needed};
	    }
	    set_hash.push_back(*it);
    }
    return vector<uint> {};
}



int main(int argc, const char * argv[]) {
    uint sum_reqd;
    if (argc < 2) {
	    cout<<"please provide valid inputs"<<endl;
    }
    else{
	    vector<uint> unsorted_list[i];
	    for(int i=1; i<=argc; i++) {
		if(i == argc)
		   sum_reqd = argv[i];  
                unsorted_list[i]= uint(argv[i]);
	    }

    }
    vector<uint> final_list = two_sum_hash(unsorted_list, 20);
    if(final_list.begin() != final_list.end()){ 
	    cout<<final_list[0]<<"\t"<<final_list[1]<<endl;
    }
    else {
	    cout<<"No matching pair"<<endl;
    }
  return 1;
}
