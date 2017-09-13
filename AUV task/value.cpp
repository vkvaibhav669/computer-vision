#include<cstdio>
#include<iostream>
using namespace std;
struct node {
double data;
struct node *link;


};
struct node *head;


void insert(double d)
{

struct node *temp=new node();
temp->data=d;
temp->link=head;
head=NULL;

//values will be stored in such a way that the values are arranged in a dynamic array

}




int main()
{
head=NULL;
double value;

//using a linked list
//so that the size constrain is not a matter

double v;
//running a while loop which will run till sensor is reciving a value 
while(value)
//when the condition that sensor recives a value is true it will run
{
cin>>v;
//reads value
insert(v);//inserting at linked list
//value will be stored in the linked list designed





}
//linkedlist will be updated as soon as the value is being recived by the sensor


return 0;
}
