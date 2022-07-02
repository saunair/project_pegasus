#include<iostream>

using namespace std;

void check_if_valid(string s){
    for(int i=0; i<s.length(); i++){
        if(s[i] !='0' && s[i]!='1'){
            throw invalid_argument("We need binary strings");
        }
    }
}


string reverse(string input_string){
    static string output_string;
    for(int i=input_string.length()-1; i>=0; i--){
        output_string.push_back(input_string[i]);
    }
    return output_string;
}


string add_binary_strings(string one, string two){
    static string solution;
    int carry_over = 0;
    int solution_length = one.length() > two.length()? one.length(): two.length();
    for(int i=solution_length -1; i>=0; i--){
        int value_first = 0;
        int value_second = 0;
        if(i<one.length()){
            value_first = int(one[i]) - '0';
        }
        if(i<two.length()){
            value_second = int(two[i]) - '0';
        }
        int ans = value_first + value_second + carry_over;
        if(ans == 2){
            carry_over = 1;
            ans=0;
        }
        if(ans == 3){
            carry_over = 1;
            ans=1;
        }
        solution.push_back(char(ans + '0'));
    }
    if(carry_over == 1){
        solution.push_back(char(1 + '0'));
    }
    return reverse(solution);
}


int main(int argc, const char* argv[]){
    string one, two;
    if(argc<3){
        throw invalid_argument("We need two strings to operate");
    }
    one = argv[1];
    two = argv[2];
    check_if_valid(one);
    check_if_valid(two);
    cout<<"Here is the added string: "<<add_binary_strings(one, two)<<endl;
    return 0;
}
