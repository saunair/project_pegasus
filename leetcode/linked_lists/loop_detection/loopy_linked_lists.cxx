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


//Defining the constructor as member functions.
//Node::Node(shared_ptr<Node> n<ext_ptr, double node_value){
//    next = next_ptr;
//    value = node_value;
//}

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


bool detect_loop(LinkedList& linked_list){
    if(linked_list.root->next == nullptr){
            cout<<"Linked list is almost empty";
            return false;
    }
    if(linked_list.root->next->next == nullptr){
	    cout<<"Linked list has only one node, the root";
	    return false;
    }
    shared_ptr<Node> second_ptr = linked_list.root->next->next; 
    shared_ptr<Node> first_ptr = linked_list.root->next; 
    int i = 0;
    while(i < 100){
        if(first_ptr == second_ptr){
                return true;
        }
        if (second_ptr == nullptr){return false;}
        if (first_ptr == nullptr){return false;}
        first_ptr = first_ptr->next;
        if(second_ptr->next != nullptr){
            second_ptr = second_ptr->next->next;
        }
        else{return false;}
        i++;
    }
    return false;

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

LinkedList loopy_linked_list(){
	LinkedList normal_ll = LinkedList();
	normal_ll.push_back(10);
	normal_ll.push_back(20);
	normal_ll.push_back(30);
	normal_ll.push_back(40);
	normal_ll.push_back(50);
	normal_ll.root->next->next = normal_ll.root;
	return normal_ll;
}


int main(int argc, const char* argv[]){
	LinkedList normal_ll = normal_linked_list();
	bool is_loopy_ll = detect_loop(normal_ll);
	if (is_loopy_ll){
		cout<<"Loop detected in the linked list";
	}
	else{
		cout<<"No loop in the linked list";
	}

	//// Now let's test a loopy linked list.
	LinkedList loopy_ll = loopy_linked_list();
	is_loopy_ll = detect_loop(loopy_ll);
	if (is_loopy_ll){
		cout<<"Loop detected in the linked list";
	}
	else{
		cout<<"No loop in the linked list";
	}
	return 0;
}
