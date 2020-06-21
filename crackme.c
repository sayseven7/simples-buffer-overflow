#include <stdio.h>
#include <string.h>

void vuln(void);


int main(void){
	vuln();
	return 0;
}



void vuln(void){
	char c[40];
	puts("Insira dados: ");
	gets(c);
	printf("Vc inserio isso: %s\n", c);
}
