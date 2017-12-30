#include <stdio.h>
#include <stdlib.h>
#include "../headers/node.h"
typedef struct{ //pointer type that indicate node
		node *head;
		int size;
}list;

list* init_list();
void appendTo(list* list, node* newnode);
void delAt(list* list,int n);
void print_list(list* list);

list* init_list(){
		list* tmp = (list*)malloc(sizeof(node));
		tmp->head = NULL;
		tmp->size = 0;
		return tmp;
}

void appendTo(list* list, node* newnode){
		if(list->head == NULL){
				list->head = newnode;
				list->size++;
		}
		else{
				node* tail = list->head;
				while(tail->next != NULL){
						tail = tail->next;
				}
				tail->next = newnode;
				list->size++;
		}
}

void delAt(list* list, int n){
		printf("\nDelete %d index of linked list\n",n);
		printf("================================\n");
		if(n<1 ||n>(list->size)){
				printf("delAT(): out of index(n = %d)\n",n);
				return;
		}
		node* tmp = list->head;
		if(n == 1){
				list->head = tmp->next;
				free(tmp);
		}
		else{
				for(int i = 1;i < n - 1;i++){
						tmp = tmp->next;
						}
						tmp->next = tmp->next->next;
		}
		list->size--;
}
void print_list(list* list){
		node *tmp = list-> head;
		printf("list size = %d\n",list->size);
		for(int n = 0;n<list->size;n++){
				printf("[%d] ",tmp->val);
				tmp = tmp->next;
		}
}
int main(int argc, char const *argv[]){
		list* linked = init_list();
		int i;
		for(i = 1; i < 6; i++){
				appendTo(linked, newnode(i));
		}
		print_list(linked);
		delAt(linked, -1);
		delAt(linked, 5);
		print_list(linked);
		delAt(linked, 3);
		print_list(linked);
		return 0;
}

