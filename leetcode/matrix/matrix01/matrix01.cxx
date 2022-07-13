#include<iostream>
#include<vector>
#include<queue>
#include<climits>

using namespace std;

vector<vector<int>> update_matrix(vector<vector<int>>& matrix){
    queue<vector<int>> zero_queue;
    vector<vector<int>> distances(matrix.size(), vector<int>(matrix[0].size(), INT_MAX));

    for(int row=0; row<matrix.size(); row++){
        for(int column=0; column<matrix[row].size(); column++){
            if(matrix[row][column] == 0){
                distances[row][column] = 0;
                zero_queue.push({row, column});
            }
        }
    }
    vector<vector<int>> combinations = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

    while(!zero_queue.empty()){
        auto indices = zero_queue.front();
        zero_queue.pop();
        int root_row = indices[0];
        int root_column = indices[1];
        for(auto d:combinations){
            int row = root_row + d[0];
            int column = root_column + d[1];
            if(row<0 || row==matrix.size() || column<0 || column==matrix[0].size()){
                continue;
            }
            if(distances[row][column] > distances[root_row][root_column] + 1){
                distances[row][column] = distances[root_row][root_column] + 1;
                // A new direction to be explored as distances have changed for row, column;
                zero_queue.push({row, column});
            }
        }
    }

    return distances;
}


void display_matrix(vector<vector<int>>& matrix){
    cout<<"Matrix:"<<endl;
    for(int row=0; row<matrix.size(); row++){
        for(int column=0; column<matrix[row].size(); column++){
            cout<<matrix[row][column]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;

}

int main(int argc, const char* argv[]){
    vector<vector<int>> a = {{0,0,0}, {0,1,0}, {1,1,1}};
    display_matrix(a);
    vector<vector<int>> b = update_matrix(a);
    display_matrix(b);
    return 0;
}
