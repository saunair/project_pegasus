#include<iostream>
#include<vector>
#include<math.h>
#include <algorithm>
#include<cctype>
#include<climits>

using namespace std;


class Point{
    public:
        int x = -INT_MIN; 
        int y = -INT_MAX;
        Point(int x_coordinate, int y_coordinate);
        Point();
};


Point::Point(){
    return;
}

Point::Point(int x_coordinate, int y_coordinate){
    x = x_coordinate;
    y = y_coordinate;
}

ostream &operator<<(ostream &os, Point const &m) {
    return os << "["<<m.x <<"\t"<<m.y<<"]"<<endl;
}

vector<Point> k_closest_points(vector<Point> all_points, Point point, int k){
   int num_points = all_points.size();
   vector<int> distances(num_points, -1);
   int point_count = 0;
   for(auto it:all_points){
       distances[point_count] = sqrt((point.x - it.x)*(point.x - it.x) + (point.y - it.y)*(point.y - it.y));
       point_count++;
   }
   
   int k_count = k;
   int index_num = 0;
   vector<Point> k_points(k);
   for(int k_count=k; k_count>0; k_count--){
       auto it_max = min_element(distances.begin(), distances.end());
       index_num = distance(distances.begin(), it_max);
       k_points[k - k_count] = all_points[index_num];
       //Remove the point entries associated to these.
       distances.erase(it_max);
       all_points.erase(all_points.begin() + index_num);
       cout<<k_points[k - k_count]<<"out"<<index_num - k<<endl;
   }
   return k_points;
}


void display_points(vector<Point> points){
    int count = 0;
    for(auto it:points){
        cout<<count<<endl;
        cout<<"point: "<<it;
        count++;
    }
}


int main(int argc, const char* argv){
    vector<Point> point_array1 = {Point(3,3), Point(5,-1), Point(-2,4)};
    Point point(0, 0);
    vector<Point> k = k_closest_points(point_array1, point, 3);
    display_points(k);
    return 0;
}
