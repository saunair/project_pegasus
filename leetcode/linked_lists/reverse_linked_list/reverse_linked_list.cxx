#include <iostream>
#include <memory>

using namespace std;


class Node{
    public:
        shared_ptr<Node> next;
        double value;
	Node(double value);
	~Node();
};


Node::Node(double node_value){
    value = node_value;
}


Node::~Node(){
	//cout<<"Node with value \t"<<value<<"\t"<<next<<"\t deleted"<<endl;
}


class LinkedList{
    public:
        shared_ptr<Node> root = nullptr;
        shared_ptr<Node> head = nullptr;
        /***
         * root -> second -> third -> fourth -> second.
         ***/
	void push_back(float data);
};


void LinkedList::push_back(float data){
    shared_ptr<Node> current_node = std::make_shared<Node>(data);
    if (root == nullptr){
        root = move(current_node);
	return;
    }
    else if(root!=nullptr and head == nullptr) {
	// We set the new node as the head and assign it as the root's next.
	head = current_node;
        root->next = head;
	return;
    }
    if(head != nullptr){
	head->next = current_node;
	head = current_node;
    }
    return;

}


LinkedList reverse_linked_list(LinkedList& linked_list){
     shared_ptr<Node> current_node = linked_list.root;
     LinkedList reversed_linked_list;
     shared_ptr<Node> previous_node;
     while(current_node != nullptr){
         shared_ptr<Node> temp = make_shared<Node>(current_node->value);
	 if(previous_node != nullptr){
	     temp->next = previous_node;
	 }
	 previous_node = temp;
	 if(reversed_linked_list.head == nullptr){
		 reversed_linked_list.head = previous_node;
	 }
	 current_node = current_node->next;
     }
     reversed_linked_list.root = previous_node;
     return reversed_linked_list;
}


LinkedList normal_linked_list(){
	LinkedList normal_ll = LinkedList();
	normal_ll.push_back(10);
	normal_ll.push_back(20);
	normal_ll.push_back(30);
	normal_ll.push_back(40);
	normal_ll.push_back(50);
	return normal_ll;
}


void display_linked_list(LinkedList* linked_list){
    shared_ptr<Node> current_node = linked_list->root;
    while(current_node != nullptr){
       cout<<current_node->value<<"\t";
       current_node = current_node->next;
    }
}


int main(int argc, const char* argv[]){
	LinkedList normal_ll = normal_linked_list();
	LinkedList reversed = reverse_linked_list(normal_ll);
	display_linked_list(&reversed);
	return 0;
}
