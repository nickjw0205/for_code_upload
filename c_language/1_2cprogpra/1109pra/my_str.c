#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *my_strcat(char *s1, const char *s2){
		
		char *temp;

		temp = (char*)malloc(strlen(s1)+strlen(s2));
		int i = 0;
		for(i = 0; i < strlen(s1);i++){
				temp[i] += s1[i];
		}
		for(int j = 0;j < strlen(s2);j++){
				temp[i+j] += s2[j];
		}

		for(int i = 0;i < strlen(temp);i++){
				s1[i] = temp[i];
		}

		return s1;
}

int my_strcmp(const char *s1, const char *s2){
		int c;
		int i = 0;	
		while(s1[i] != '\0' || s2[i] != '\0'){
				if(s1[i++] != s2[i++]){
						break;
				}
		}
		c = (s1[i] - s2[i]);
		return c;
}


int main(){
		char *str1 = "STARBUCKS";
		char str2[10] = "STAR";
		char *str3 = "BUCKS";
		my_strcat(str2,str3);
		if(my_strcmp(str1,str2)==0){
				printf("Nailed it!\n");
		}
		else{
				printf("my_strcmp(str1,str2): %d\n",my_strcmp(str1,str2));
		}
		return 0;
}
