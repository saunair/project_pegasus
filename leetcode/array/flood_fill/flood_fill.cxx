#include<iostream>
#include<vector>

using namespace std;

vector<vector<int>> get_image(){
    vector<vector<int>> image = {{0, 0, 0, 0, 0, 0, 0, 0},
	                         {0, 0, 1, 2, 3, 4, 5, 6},
				 {1, 0, 3, 4, 5, 3, 5, 5},
				 {2, 0, 3, 2, 54, 5, 5, 4}};
    return image;
}


void fill_location(int row, int col, vector<vector<bool>>& visited, vector<vector<int>>& image, int fill_value){
        int up = row - 1;
        int down = row + 1;
        int right = col + 1;
        int left = col - 1;

	visited[row][col] = true;
        if(up>-1){
	    if(image[row][col] == image[up][col] && !visited[up][col]){
	        fill_location(up, col, visited, image, fill_value);
	    }
	}
        if(down<image.size()){
	    if(image[row][col] == image[down][col] && !visited[down][col]){
	        fill_location(down, col, visited, image, fill_value);
	    }
	}
        if(right<image[0].size()){
       	    if(image[row][col] == image[row][right] && !visited[row][right]){
	        fill_location(row, right, visited, image, fill_value);
	    }
	}
        if(left>-1){
	    if(image[row][col] == image[row][left] && !visited[row][left]){
	        fill_location(row, left, visited, image, fill_value);
	    }
	}
	image[row][col] = fill_value;
    return;
}



void flood_fill(vector<vector<int>>& image, int row, int col, int fill_value){
	const int rows = image.size();
	const int cols = image[0].size();
	vector<vector<bool>> visited(rows, vector<bool>(cols, false));
	fill_location(row, col, visited, image, fill_value);

}

void display_image(vector<vector<int>>& image){
    for(vector<vector<int>>::iterator row_it = image.begin(); row_it!=image.end(); row_it++){
	    for(vector<int>::iterator col_it = row_it->begin(); col_it!=row_it->end(); col_it++){
		    cout<<*col_it<<"\t";
	    }
	    cout<<endl;
    }
}


int main(int argc, const char* argv[]){
    vector<vector<int>> image = {{0, 0, 0, 0, 0, 0, 0, 0},
	                         {0, 0, 1, 2, 3, 4, 5, 6},
				 {1, 0, 3, 4, 5, 3, 5, 5},
				 {2, 0, 3, 2, 54, 5, 5, 4}};
    flood_fill(image, 2, 1, 100);
    display_image(image);
}
