#include <stdio.h>
#include <stdlib.h>
#include "../headers/node.h"

typedef struct{
		node *front;
		int size;
		node* rear;
}queue;

queue* init_queue();
void enqueue(queue*, node*);
void dequeue(queue*);
void front(queue*);
void print_queue(queue*);

queue *init_queue(){
		queue* tmp = malloc(sizeof(queue));
		tmp->front = NULL;
		tmp->rear = NULL;
		tmp -> size = 0;
		return tmp;
}

void enqueue(queue* que, node* newnode){
		if(que->front == NULL){
				que->front = newnode;
				que->rear = newnode;
				que->size++;
		}
		else{
				que->rear->next = newnode;
				que->rear = newnode;
				que->size++;
		}
}

void dequeue(queue* que){
		if(que->front == NULL){
				printf("dequeue(): queue id empty\n");
		}
		else{
				que->front = que->front->next;
				que->size--;
		}
}

void front(queue* que){
		if(que->front == NULL){
				printf("\nfront(): queue is empty\n");
				
		}
		else{
				printf("front: %d\n",que->front->val);
		}
}

void print_queue(queue* que){
		node* tmp = que-> front;
		printf("Q: ");
		for(int i = 0;i < que->size;i++){
				printf("[%d] ", tmp->val);
				tmp = tmp->next;
		}
}



int main(int argc, char const *argv[]){
		int i;
		queue* q = init_queue();
		enqueue(q, newnode(1));
		front(q);
		dequeue(q);
		dequeue(q);
		for(i = 2;i < 6; i++){
				enqueue(q, newnode(i));
		}
		dequeue(q);
		print_queue(q);
		for(i = 0; i < 3; i++) dequeue(q);
		front(q);
		return 0;
}

