#include<iostream>
#include<queue>
#include<vector>

using namespace std;


void display_matrix(vector<vector<int>>& matrix){
    for(int row=0; row<matrix.size(); row++){
        for(int column=0; column<matrix[row].size(); column++){
            cout<<matrix[row][column]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
}

vector<vector<int>>& example_1(){
    static vector<vector<int>> a = {
        {2,1,1},
        {1,1,0},
        {0,1,1}
    };
    return a;
}


vector<vector<int>>& example_2(){
    static vector<vector<int>> a = {
        {2,1,1},
        {0,1,1},
        {1,0,1}
    };
    return a; }


int rotting_oranges(auto& rotten_queue, auto& matrix){
    int touched = 0;
    while(!rotten_queue.empty()){
        vector<int> a = rotten_queue.front(); 
        rotten_queue.pop();
        int row = a[0];
        int column = a[1];
        if(row == -1){
            //We've reached the delimiter.
            return touched;
        }
        int up = row -1;
        int down = row + 1;
        int right = column - 1;
        int left = column + 1;
        vector<vector<int>> combinations = {{up, column}, {down, column}, {row, right}, {row, left}};
        for(int i=0; i<combinations.size(); i++){
            int row_child = combinations[i][0];
            int column_child = combinations[i][1];
            if(row_child <0 || row_child >= matrix.size() || column_child<0 || column_child>=matrix[1].size()){
                continue;
            }
            if(matrix[row_child][column_child] == 1){
                matrix[row_child][column_child] = 2;
                vector<int> a = {row_child, column_child};
                rotten_queue.push(a);
                touched = 1;
            }
        }
    }
    return touched;
}


int time_all_rotten_oranges(vector<vector<int>>& matrix){
    queue<vector<int>> rotten_queue;
    for(int row=0; row<matrix.size(); row++){
        for(int column=0; column<matrix[row].size(); column++){
            if(matrix[row][column] == 2){
                vector<int> a = {row, column};
                rotten_queue.push(a);
            }
        }
    }
    vector<int> a= {-1, -1};
    rotten_queue.push(a);
    int time = 0;
    while(rotten_queue.size()>1){
        time += rotting_oranges(rotten_queue, matrix);
        display_matrix(matrix);
        //cout<<rotten_queue.front()[0]<<" "<<rotten_queue.front()[1]<<endl;
        vector<int> a= {-1, -1};
        rotten_queue.push(a);
    }
    //Check if we have any normal oranges left after the breath first search;
    for(int row=0; row<matrix.size(); row++){
        for(int column=0; column<matrix[row].size(); column++){
            if(matrix[row][column] == 1){
                return -1;
            }
        }
    }
    return time;
}


int main(int argc, const char* argv[]){
    auto eg1 = example_1();
    auto eg2 = example_2();
    cout<<"Time to take for rotting: "<<time_all_rotten_oranges(eg1)<<endl;
    cout<<"Time to take for rotting: "<<time_all_rotten_oranges(eg2)<<endl;
    return 0;
}
