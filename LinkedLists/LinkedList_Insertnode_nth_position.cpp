//g++  7.4.0

#include <iostream>

struct Node {
    int data;
    Node* next;
};

struct Node* head;

void Insert(int x, int n){
    Node* temp1 = new Node();
    temp1 -> data = x;
    temp1 -> next = NULL;
    
    if(n==1){
        temp1->next = head;
        head = temp1;
        return;
    }
    
    Node* temp2= head;
    
    for(int i=0;i<n-2;i++){
        
        temp2 = temp2->next;
    }
    
    temp1->next = temp2->next;
    temp2->next = temp1;
    
}

void Print(){
    Node* temp = head;
    while(temp!= NULL){
        printf("%d  ",temp->data);
        temp = temp->next;
    }
    printf("\n");
    
}


int main()
{
    head = NULL;
    Insert(100,1);
    Print();
    Insert(200,2);
    Print();
    Insert(300,3);
    Print();
    Insert(400,2);
    Print();

}
