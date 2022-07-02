#include<iostream>
#include<memory>

using namespace std;

class Node{
    public:
        double value;
        shared_ptr<Node> left = nullptr;
        shared_ptr<Node> right = nullptr;
        Node(double node_value): value(node_value){}
        Node(double node_value, shared_ptr<Node> left_node): value(node_value), left(left_node){} 
        Node(double node_value, shared_ptr<Node> left_node, shared_ptr<Node> right_node): value(node_value), right(right_node), left(left_node){} 
};


class BinaryTree{
    public:
        shared_ptr<Node> root;
};


BinaryTree* test_bt(){
    auto left1 = make_shared<Node>(4);
    auto left0 = make_shared<Node>(4, left1);
    auto right0 = make_shared<Node>(6);
    auto root = make_shared<Node>(5, left0, right0);
    static BinaryTree our_bt;
    our_bt.root = root;
    return &our_bt;
}


int max_depth(shared_ptr<Node> node){
    int soln = 0;
    int left_depth = 0;
    int right_depth = 0;
    if(node->left != nullptr){
        left_depth = max_depth(node->left) + 1;
    }
    if(node->right != nullptr){
        right_depth = max_depth(node->right) + 1;
    }
    return left_depth >= right_depth ? left_depth: right_depth;
}



int main(int argc, const char* argv[]){
    BinaryTree* bt = test_bt();
    cout<<"The maximum depth is: "<<max_depth(bt->root)<<endl;
    return 0;
}
