#include <stdio.h>
#include <stdlib.h>
#include "../headers/node.h"

typedef struct{
		node* top;
		int size;
}stack;

stack* init_stack();
void push(stack*, node*);
void pop(stack*);
void top(stack*);
void print_stack(stack*);

stack* init_stack(){
		stack* tmp = malloc(sizeof(stack));
		tmp-> top = NULL;
		tmp->size = 0;
		return tmp;
}

void push(stack* st, node* newnode){
		if(st->top == NULL){
				st->top = newnode;
				st->size++;
		}
		else{
				newnode->next = st->top;
				st->top = newnode;
				st->size++;
		}
}
void pop(stack* st){
		if(st->top == NULL){
				printf("pop(): stack is empty\n");
		}
		else{
				st->top = st->top-> next;
				st->size--;
		}
}
void top(stack* st){
		if(st->top == NULL){
				printf("\ntop(): stack is empty.\n");
		}
		else{
				printf("front: %d\n",st->top->val);
		}
}

void print_stack(stack* st){
		node *tmp = st-> top;
		printf("Top\n");
		for(int i = 0;i < st->size; i++){
				printf("[%d]\n",tmp->val);
				tmp = tmp->next;
		}
}
		



int main(int argc, char const *argv[]){
		int i;
		stack* s = init_stack();
		push(s, newnode(1));
		top(s);
		pop(s);
		pop(s);
		for(i = 2; i < 6;i++){
				push(s, newnode(i));
		}
		pop(s);
		print_stack(s);
		for(i = 0; i < 3; i++) pop(s);
		top(s);
		return 0;
}

