#include<iostream>
#include<memory>
#include<queue>

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
    auto left1 = make_shared<Node>(4);
    auto left0 = make_shared<Node>(4, left1);
    auto right0 = make_shared<Node>(6);
    auto root = make_shared<Node>(5, left0, right0);
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


int height_of_tree(shared_ptr<Node>& root){
    if(root == nullptr){
        return 0;
    }
    return 1 + max(height_of_tree(root->left), height_of_tree(root->right));
}


int diameter_of_tree(shared_ptr<Node>& root){
    if(root == nullptr){
        return 0;
    }
    int height_left = height_of_tree(root->left);
    int height_right = height_of_tree(root->right);

    int diameter_left = diameter_of_tree(root->left);
    int diameter_right = diameter_of_tree(root->right);

    return max(height_left + height_right +1, max(diameter_left, diameter_right));
}


int main(int argc, const char* argv[]){
    BinaryTree bt = test_bt();
    display_binary_tree(bt);
    cout<<diameter_of_tree(bt.root)<<endl;
    return 0;
}
