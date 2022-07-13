#include <iostream>
#include <memory>
#include<cctype>
#include<cfloat>

using namespace std;


class Node{
    public:
        shared_ptr<Node> next = nullptr;
        shared_ptr<Node> previous = nullptr;
        double value;
        int key;
	Node(double value);
};


Node::Node(double node_value){
    value = node_value;
}


class LruCache{
    public:
        shared_ptr<Node> root = nullptr;
        shared_ptr<Node> head = nullptr;
        int capacity;
        /***
         * root -> second -> third -> fourth -> second.
         ***/
	double get(int key);
	void set(int key, double value);
    LruCache(double intake_capacity): capacity(intake_capacity){};
};


void LruCache::set(int key, double data){
    if(capacity > 0){
        capacity = --capacity;
        cout<<capacity<<endl;
    }
    else if(capacity <= 0){
        root = root->next;
        root->previous = nullptr;
    }

    if(head!=nullptr){
        auto temp = make_shared<Node>(data);
        head->next =  temp;
        temp->previous = head;
        temp->key = key;
        head = temp;
    }
    else{
        head = make_shared<Node>(data); 
        root = head;
    }
}


double LruCache::get(int key){
    shared_ptr<Node> node = head;
    double value = -1;
    while(node != nullptr){
        if(node->key == key){
            value = node->value;
            shared_ptr<Node> next = node->next;
            shared_ptr<Node> previous = node->previous;
            if(node->previous !=nullptr){
                node->previous->next = next;
            }
            if(node->next !=nullptr){
                node->next = previous;
            }
            head->next = node;
            head = node;
            node->next = nullptr;
            return value;
        }
        node = node->previous;
    }
    return value;
}


int main(int argc, const char* argv[]){
    static LruCache lru_cache = LruCache(5);
    lru_cache.set(5, 10.0);
    cout<<"without key:"<<lru_cache.get(3)<<endl;
    lru_cache.set(3, 20.0);
    lru_cache.set(4, 20.0);
    lru_cache.set(5, 20.0);
    lru_cache.set(6, 20.0);
    lru_cache.set(7, 20.0);
    lru_cache.set(8, 40.0);
    lru_cache.set(9, 20.0);
    cout<<"without key:"<<lru_cache.get(8)<<endl;
	return 0;
}
