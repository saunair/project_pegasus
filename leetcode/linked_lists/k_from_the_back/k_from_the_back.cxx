#include <iostream>
#include <memory>

using namespace std;


class Node{
    public:
        shared_ptr<Node> next;
        double value;
	Node(double value);
};


Node::Node(double node_value){
    value = node_value;
}


class LinkedList{
    public:
        shared_ptr<Node> root = nullptr;
        shared_ptr<Node> head = nullptr;
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


LinkedList& normal_linked_list(){
	static LinkedList normal_ll = LinkedList();
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


int kth_element_from_tail(LinkedList& linked_list, int k=0)
{ 
   shared_ptr<Node> first_ptr= nullptr;
   shared_ptr<Node> second_ptr=linked_list.root; 
   int num_elements = 0;
   while(second_ptr->next!=nullptr){
       if(num_elements>=k){
           // The higher pointer has covered the window
           first_ptr = first_ptr->next;
       }
       second_ptr = second_ptr->next;
       num_elements++;
   }
   if(first_ptr == nullptr){
       throw length_error("Length isn't accurate");
   }
   return first_ptr->value;
}


int main(int argc, const char* argv[]){
	LinkedList normal_ll = normal_linked_list();
    int element = 6;
    int soln = kth_element_from_tail(normal_ll, element);
    cout<<"our answer is :"<<soln<<endl;
	//display_linked_list(normal_linked_list);
	return 0;
}
