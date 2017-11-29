#include <stdio.h>

#define GREETINGS(a, b, c) \
	printf(#a", " #b ", and " #c ": Hello!\n")

#define WRONG_DREETINGS(a, b, c) \
	printf("a, b, c : Hello!\n")

#define EXEC(x) func_##x()

void func_A(){
		printf("This is func_A()\n");
}

void func_B(){
		printf("This is func_b()\n");
}

int main(){
		GREETINGS(Alice, Bob, Carole);
		WRONG_GREETINGS(Alice, Bob, Carole);

		EXEC(A);
		EXEC(B);

		return 0;
}


