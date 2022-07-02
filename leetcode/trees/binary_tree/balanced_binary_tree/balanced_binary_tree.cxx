


#include<iostream>
#include <stdlib.h>

using namespace std; 

/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


TreeNode* balanced_tree(){
    /***
     * A balanced tree. 
     ***/
    TreeNode* left = new TreeNode(100);
    TreeNode* right = new TreeNode(2);
    TreeNode* my_root = new TreeNode(1, left, right);
    return my_root;
}


TreeNode* imbalanced_tree(){
    /***
     * An imbalanced tree with two nodes in depth added to the right side.
     ***/
    TreeNode* left = new TreeNode(100);
    TreeNode* right_right_right = new TreeNode(56);
    TreeNode* right_right = new TreeNode(500, right_right, nullptr);
    TreeNode* right = new TreeNode(2, nullptr, right_right);
    TreeNode* my_root = new TreeNode(1, left, right);
    return my_root;
}


class Solution {
    private:
        int max_depth(TreeNode* node){
	    int left_depth=0;
	    int right_depth=0;
	    //If a child exists, check the depth of the child and add 1 to it.
	    if(node->left != nullptr){
                left_depth = max_depth(node->left) + 1;
	    }
	    if(node->right != nullptr){
	        right_depth = max_depth(node->right) + 1;
	    }
	    return std::max(left_depth, right_depth);
        }
    public:
        bool isBalanced(TreeNode* root) {
            int right_depth = 0;
            int left_depth = 0; 
	    if(root->right != nullptr){
		right_depth = max_depth(root->right);
	    }
	    if(root->left != nullptr){
		left_depth = max_depth(root->left);
	    }
	    //For a balanced tree, the depth of both children must not exceed by 1.
    	    if(std::abs(right_depth - left_depth) > 1){
    	        return 0;
    	    }
    	    return 1;
        }
};


int main(int argc, const char* argv[]){
    TreeNode *eg_balanced_tree = balanced_tree();
    Solution my_solver = Solution();
    //int is_balanced = my_solver.isBalanced(eg_balanced_tree);
    //cout<<"Is balanced:"<<is_balanced<<endl;
    eg_balanced_tree = imbalanced_tree();
    int is_balanced = my_solver.isBalanced(eg_balanced_tree);
    cout<<"Is balanced:"<<bool(is_balanced)<<endl;
    return 0;
}
