#include <iostream>

#include <array>
using namespace std;

const int NUM_ROWS = 4;
const int NUM_COLS = 5;

array<array<bool, NUM_COLS>, NUM_ROWS> array_grid = {{
  {1,1,0,0,0},
  {1,1,0,0,0},
  {1,1,1,1,0},
  {0,0,0,1,1}
}};


bool fill_position_if_valid(
    array<array<bool, NUM_COLS>, NUM_ROWS> &visited_array, 
    array<array<bool, NUM_COLS>, NUM_ROWS> &island_array, 
    int row, int column
){
	if(row>=0 && column>=0 && row<NUM_ROWS && column<NUM_COLS){
            if(island_array[row][column] == 1){
               visited_array[row][column] = 1; 
	       return 1;
	    } 
	    if(island_array[row][column] == 0){
		    visited_array[row][column] = 1;
		    return 0;
	    }
	}
    return 0;
}


void fill_out_cluster(
    array<array<bool, NUM_COLS>, NUM_ROWS> &visited_array, 
    array<array<bool, NUM_COLS>, NUM_ROWS> &island_array, 
    int row, int column
){
    if(visited_array[row][column] == 1){
	    return;
    }
    if(!fill_position_if_valid(visited_array, island_array, row, column)){
	    return;
    }
    int up = row-1;
    int down = row+1;
    int left = column-1;
    int right = column+1;
    //The current function is taking care of the validity of the indices.
    //This is depth search for the daughter nodes.
    fill_out_cluster(visited_array, island_array, up, column);
    fill_out_cluster(visited_array, island_array, down, column);
    fill_out_cluster(visited_array, island_array, row, right);
    fill_out_cluster(visited_array, island_array, row, left);
}


int num_islands(array<array<bool, NUM_COLS>, NUM_ROWS> &island_array){
    //Assuming the size here for now.
    array<array<bool, NUM_COLS>, NUM_ROWS> visited_array = {
	    {{0, 0, 0, 0, 0}, {0, 0, 0, 0, 0}, {0, 0, 0, 0, 0}, {0, 0, 0, 0, 0}}
    };
    int total_islands = 0;

    for(int row=0; row<NUM_ROWS; row++){
        for(int column=0; column<NUM_COLS; column++){
	   if(island_array[row][column] == 1 && !visited_array[row][column]){
               fill_out_cluster(visited_array, island_array, row, column);
	       total_islands++;
	   } 
	}
    }
    return total_islands;
}


int main(int argc, const char* argv[]){
    int total_islands = num_islands(array_grid);
    cout<<"The number of islands are: "<<total_islands<<endl;
    return 0;
}
