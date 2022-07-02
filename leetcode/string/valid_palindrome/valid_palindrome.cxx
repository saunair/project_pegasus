#include<iostream>
#include <cwctype>
#include <cctype>

using namespace std;


string convert_string(string input_string){
    string output_string;
    for(int i=0; i<input_string.length(); i++){
        if(iswalnum(input_string[i])){
            output_string.push_back(tolower(input_string[i]));
        }
    }
    return output_string;
}


bool check_palindrome(string input_string){
    input_string = convert_string(input_string);
    int end_index = input_string.length() -1;
    for(int start_index=0; start_index<input_string.length(); start_index++){
        //cout<<input_string[start_index]<<"\t"<<input_string[end_index - start_index]<<endl;
        if(input_string[start_index] != input_string[end_index - start_index]){
            return false;
        } 
    }
    return true;
}


int main(int argc, const char* argv[]){
    string test_string_1 = "A man, a plan, a canal: Panama";
    string test_string_2 = "race a car";
    cout<<test_string_1<<check_palindrome(test_string_1)<<endl;
    cout<<test_string_2<<check_palindrome(test_string_2)<<endl;
    return 0;
}
