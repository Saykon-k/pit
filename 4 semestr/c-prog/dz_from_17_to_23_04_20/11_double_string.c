#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void double_ke(char *str){
  int i = 0 ;
  while(str[i] != '\0'){
    i++;
  }
  int k = 0;
  while(k < i){
    str[k+i] = str[k];
    k++;
  }
}

int main() {
  char str[40];
  scanf("%39s", str);
  double_ke(str);
  printf("%s\n",str );
   scanf("%39s", str);
  return 0;
}
