#include<iostream>
#include<memory>

using namespace std;


class Node{
    public:
        shared_ptr<Node> next;
	double value;
	Node(double insert_value);
};

Node::Node(double insert_value){
    value = insert_value;
}


class LinkedList{
    public:
       shared_ptr<Node> root = nullptr;
       shared_ptr<Node> tail = nullptr;
       void push(double value);
};


void LinkedList::push(double value){
    shared_ptr<Node> current_node = make_shared<Node>(value);
    if(root == nullptr){
        root = current_node;
	return;
    }
    if(tail == nullptr){
        tail = current_node;
	root->next = tail;
	return;
    }
    tail->next = current_node;
    tail = current_node;
}


LinkedList first_linked_list(){
    LinkedList linked_list;
    linked_list.push(0);
    linked_list.push(2);
    linked_list.push(4);
    linked_list.push(6);
    return linked_list;
}


LinkedList second_linked_list(){
    LinkedList linked_list;
    linked_list.push(1);
    linked_list.push(3);
    linked_list.push(5);
    linked_list.push(7);
    return linked_list;
}


LinkedList merge_linked_lists(LinkedList& linked_list_1, LinkedList& linked_list_2){
    shared_ptr<Node> list1 = linked_list_1.root;
    shared_ptr<Node> list2 = linked_list_2.root;
    LinkedList soln;
    while(1){
        if(list1 == nullptr){
            if(list2 == nullptr){
                break;
            }
            soln.push(list2->value);
            list2 = list2->next;
	    continue;
        }
	if(list2 == nullptr){
            soln.push(list1->value);
            list1 = list1->next;
	    continue;
	}
        if(list1->value < list2->value){
            soln.push(list1->value);
            list1 = list1->next;
	    continue;
        }
	else if(list1->value >= list2->value){
            soln.push(list2->value);
            list2 = list2->next;
	    continue;
        }
    }
    return soln;
}


void display_list(LinkedList list){
    shared_ptr<Node> node = list.root;
    while(node != nullptr){
        cout<<node->value<<"\t";
	node = node->next;
    }
    cout<<endl;
}


int main(int argc, const char* argv[]){
    LinkedList first_ll = first_linked_list();
    LinkedList second_ll = second_linked_list();
    LinkedList solution = merge_linked_lists(first_ll, second_ll);
    display_list(solution);
}
