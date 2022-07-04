#include<iostream>
#include<map>

using namespace std;


bool is_note_possible(string ransom_note, string option_string){
    map<char, int> char_count;
    for(int i=0; i<option_string.length(); i++){
        if(char_count[option_string[i]]){
            char_count[option_string[i]]++;
        }
        else{
            char_count[option_string[i]] = 1;
        }
        
    }
    for(int i=0; i<ransom_note.length(); i++){
        if(char_count[option_string[i]]){
            char_count[option_string[i]]--;
        }
        else if(!char_count[option_string[i]]){
            return false;
        }
        else if(char_count[option_string[i]] <=0){
            return false;
        }
    }
    return true;

}


int main(int argc, const char* argv){
    string ransom_note = "this is the end";
    cout<<"Is ransom possible"<<is_note_possible(ransom_note, "end this is the not of course")?"Yes":"No"<<endl;
    return 0;
}
