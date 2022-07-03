#include<iostream>
#include<stack>
#include<map>

using namespace std;

bool valid_parenthesis(string& input_string){
    map<char, char> hash = {{'{', '}'}, {'(', ')'}, {'[', ']'}};
    stack<char> our_stack;
    for(int i=0; i<input_string.length(); i++){
        if (our_stack.empty()==true ){
            our_stack.push(input_string[i]);
        }
        else if(hash[our_stack.top()] == input_string[i]){
            our_stack.pop();
        }
        else{
            our_stack.push(input_string[i]);
        }
    }
    if(our_stack.empty()){
        return true;
    }
    return false;
}



int main(int argc, const char* argv[]){
    string input_string = argv[1];
    cout<<valid_parenthesis(input_string);
    return 0;
}
