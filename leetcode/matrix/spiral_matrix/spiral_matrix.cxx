#include<iostream>
#include<vector>
#include<climits>

using namespace std;


class Index{
    public:
        int row; 
        int column;
        Index(int x, int y);
        Index();
};


Index::Index(int x, int y){
    row = x;
    column = y;
}
Index::Index(){
    row = INT_MAX;
    column = INT_MIN;
}


ostream &operator<<(ostream &os, Index const &m){
    return os << "["<<m.row <<"\t"<<m.column<<"]"<<endl;
}


void print_matrix(vector<vector<float>> matrix, vector<Index> indices){
    for(auto& index: indices){
        if(index.row < matrix.size() and index.row >=0){
            if(index.column < matrix[index.row].size() and index.column >=0){
                cout<<matrix[index.row][index.column]<<"\t";
            }
        }
    }
    cout<<endl;
}


vector<Index> spiral_indices(int rows, int columns){
    vector<bool> b(columns, false);
    vector<vector<bool>> visited(rows, b); 
    vector<int> dir_row = {{0, 1, 0, -1}};
    vector<int> dir_column = {{1, 0, -1, 0}};
    int dir = 0;
    int total_elements = rows*columns;
    int row = 0;
    int column = 0;
    int c_row = 0;
    int c_column = 0;
    vector<Index> spiral(total_elements); 
    for(int current_element=0; current_element<total_elements; current_element++){
        // We switch the directions if we hit the upper limit or the covered radius of elements.
        visited[row][column] = true;
        spiral[current_element] = Index(row, column);
        c_row  = row + dir_row[dir];
        c_column = column + dir_column[dir];
        if(c_row < rows and c_column < columns and c_row>=0 and c_column>=0 and visited[c_row][c_column] == false){
            row = c_row;
            column = c_column;
        }
        else{
            //Change the direction of search.
            dir = (dir + 1) % 4;
            row += dir_row[dir];
            column += dir_column[dir];
        }
    }
    return spiral;
}


int main(int argc, const char* argv[]){
    vector<vector<float>> test_matrix_small = {{1.0, 2.0, 3.0}, {4.0, 5.0, 6.0}, {7.0, 8.0, 9.0}};
    vector<vector<float>> test_matrix_big = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
    vector<Index> mock_indices = {Index(0, 0), Index(3, 3)};
    vector<Index> a = spiral_indices(test_matrix_small.size(), test_matrix_small[0].size());
    print_matrix(test_matrix_small, a);
    a = spiral_indices(test_matrix_big.size(), test_matrix_big[0].size());
    print_matrix(test_matrix_big, a);
    return 0;
}
