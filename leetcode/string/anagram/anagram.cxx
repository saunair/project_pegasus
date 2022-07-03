#include<iostream>
#include<map>

using namespace std;

map<char,int> get_char_count(string input_string){
    map<char, int> char_count;
    for(int i=0; i<input_string.length(); i++){
        char_count[input_string[i]]++;
    }
    return char_count;
}



bool is_anagram(string string1, string string2){
    if(string1.length()!=string2.length()){
        return false;
    }
    map<char, int> char_count1 = get_char_count(string1);
    map<char, int> char_count2 = get_char_count(string2);
    for(int i=0; i<string1.length(); i++){
        if(char_count1[string1[i]] != char_count2[string1[i]]){
            return false;
        }
    }

    return true;
}


int main(int argc, const char* argv[]){
    string test_string1 = "anagram";
    string test_string2 = "fagaram";
    cout<<is_anagram(test_string1, test_string2);
    return 0;
}
