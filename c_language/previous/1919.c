#include <stdio.h>
#include <string.h>

int count[2][26] = {0};

int min(int a, int b){
	// 삼항연산
	return a < b? a:b;
}

int main(){
	char str1[1001];
	char str2[1001];
	scanf("%s", str1);
	scanf("%s", str2);

	int len1 = strlen(str1);
	int len2 = strlen(str2);

	int result = 0;

	// 글자 카운트
	for(int i = 0; i < len1; i++){
		count[0][str1[i]-'a']++;
	}
	for(int i = 0; i < len2; i++){
		count[1][str2[i]-'a']++;
	}

	// 교집합을 구해서 빼야할 개수 카운팅

	for(int i = 0; i < 26; i++){
		int pivot = min(count[0][i], count[1][i]);
		result += (count[0][i] - pivot + count[1][i] - pivot);
	}

	printf("%d\n", result);


	return 0;
}