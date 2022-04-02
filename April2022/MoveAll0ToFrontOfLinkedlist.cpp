//User function Template for C++
/* Linked List Node structure
struct Node
{
    int data;
    struct Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
    
};
*/
// Move Zeros to the front of the list
void moveZeroes(struct Node **head)
{
    //Your code here
     Node*x=*head;
   Node*curr=*head;
   
   Node*prev=*head;
   curr=curr->next;
   
   while(curr)
   {
       if(curr->data==0)
       {
           x=curr;
           curr=curr->next;
           x->next=*head;
           prev->next=curr;
           
           *head=x;
           
       }
       else{
          prev=curr;
           curr=curr->next;
         
       }
   }
}