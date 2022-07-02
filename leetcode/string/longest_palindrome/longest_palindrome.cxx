/***
 * Find the longest palindrome possible with a list of characters.
 *
 */

#include<iostream>
#include<set>

using namespace std;

string test_string(){
    return "dcccdab";
}


int check_palindrome(string characters){
    int num_characters = characters.length();
    set<char> set_chars;
    int count = 0;
    for(int index=0; index<num_characters; index++){
        set<char>::iterator location = set_chars.find(characters[index]);
        if(location != set_chars.end()){
            set_chars.erase(location);
            count = count+2;
        }
        else{
            set_chars.insert(characters[index]);
        }
    }
    return ++count;
}


int main(int argc, const char* argv[]){
    string a;
    if(argc >1){
        a = argv[1];
        if(argc>2){cout<<"You have provided way too many strings. We're using only the first one now."<<endl;}
    }
    else{
        a = test_string();
    }
	int solution = check_palindrome(a);
    cout<<"Longest palindrome possible is: "<<solution<<endl;
	return 0;
}
