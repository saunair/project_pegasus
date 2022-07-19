#include<iostream>
#include<memory>
#include<vector>
#include<queue>
#include<climits>


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


BinaryTree test_bt(){
    auto left10 = make_shared<Node>(4);
    auto right10 = make_shared<Node>(6);
    auto left11 = make_shared<Node>(14);
    auto right11 = make_shared<Node>(16);
    auto left13 = make_shared<Node>(19);
    auto right13 = make_shared<Node>(12);
    auto left12 = make_shared<Node>(20);
    auto right12 = make_shared<Node>(21);
    auto left01 = make_shared<Node>(15, left10, right10);
    auto right01 = make_shared<Node>(17, left11, right11);
    auto left00 = make_shared<Node>(5, left13, right13);
    auto right00 = make_shared<Node>(7, left12, right12);
    auto left = make_shared<Node>(1, left00, right00);
    auto right = make_shared<Node>(2, left01, right01);
    auto root = make_shared<Node>(3, left, right);
    static BinaryTree our_bt;
    our_bt.root = root;
    return our_bt;
}


void populate_queue(shared_ptr<Node>& root, queue<double>& binary_tree_queue){
    //Adding for the root node. If not we've already added this value due to the following daughter traversal code.
    if(binary_tree_queue.empty()){
        binary_tree_queue.push(root->value);
    }
    if(root->left != nullptr){
        binary_tree_queue.push(root->left->value);
    }
    if(root->right!=nullptr){
        binary_tree_queue.push(root->right->value);
    }
    if(root->left != nullptr){
        populate_queue(root->left, binary_tree_queue);
    }
    if(root->right!=nullptr){
        populate_queue(root->right, binary_tree_queue);
    }
}


void display_binary_tree(BinaryTree& tree){
    queue<double> binary_tree_queue;
    populate_queue(tree.root, binary_tree_queue);
    while(!binary_tree_queue.empty()){
        double a = binary_tree_queue.front();
        cout<<a<<" ";
        binary_tree_queue.pop();
    }
    cout<<endl;
}


bool get_path_to_node(
        shared_ptr<Node> root, 
        double value, vector<double>& path
){ 
    if(root == nullptr){ 
        return false;
    }
    path.push_back(root->value);
    if(root->value == value){
        return true;
    }
    bool lpath = get_path_to_node(root->left, value, path);
    bool rpath = get_path_to_node(root->right, value, path);
    if(lpath == true || rpath == true){
        return true;
    }
    path.erase(path.end()-1);
}


int lowest_common_ancestor(double first, double second, shared_ptr<Node> root){
    if(root == nullptr){
        return INT_MIN;
    } 
    if(root->value == first || root->value == second){
        return root->value;
    }
    int lpath = lowest_common_ancestor(first, second, root->left);
    int rpath = lowest_common_ancestor(first, second, root->right);
    if(lpath != INT_MIN && rpath != INT_MIN){
        return root->value; 
    }
    if(lpath !=INT_MIN){
        return lpath;
    }
    return rpath;
}


int main(int argc, const char* argv[]){
    BinaryTree bt = test_bt();
    //display_binary_tree(bt);
    cout<<"The lowest common ancestor is: "<<lowest_common_ancestor(5, 7, bt.root)<<endl;

    return 0;
}
