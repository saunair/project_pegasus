#include<iostream>
#include<vector>
#include<math.h>
#include <algorithm>

using namespace std;


vector<vector<int>> k_closest_points(vector<vector<int>> all_points, vector<int> point, int k){
   int num_points = all_points.size();
   vector<int> distances(num_points, -1);
   int point_count = 0;
   for(vector<vector<int>>::iterator it=all_points.begin(); it!=all_points.end(); ++it){
       distances[point_count] = sqrt((point[0] - (*it)[0])*(point[0] - (*it)[0]) + (point[1] - (*it)[1])*(point[1] - (*it)[1]));
       point_count++;
   }
   
   int k_count = k;
   int index_num = 0;
   vector<vector<int>> k_points(k);
   for(int k_count=k; k_count>0; k_count--){
       auto it_max = min_element(distances.begin(), distances.end());
       index_num = distance(distances.begin(), it_max);
       k_points[index_num] = all_points[index_num];
       distances.erase(it_max);
       all_points.erase(all_points.begin() + index_num);
   }
   return k_points;
}


void display_points(vector<vector<int>> points){
    int count = 0;

    for(vector<vector<int>>::iterator it=points.begin(); it!=points.end(); ++it){
        cout<<count<<endl;
        cout<<"point: ["<<(*it)[0]<<"\t"<<(*it)[1]<<"]"<<endl;
        count++;
    }
}


int main(int argc, const char* argv){
    vector<vector<int>> point_array1 = {{3,3}, {5,-1}, {-2,4}};
    vector<int> point(2, 0);
    vector<vector<int>> k = k_closest_points(point_array1, point, 3);
    display_points(k);
    return 0;
}
