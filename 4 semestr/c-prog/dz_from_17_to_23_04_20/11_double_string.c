#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void double_ke(char *s){
  int i = 0 ;
  while(s[i] != '\0'){
    i++;
  }
  char le[100] = "";
  strcat(le,s);
  strcat(s,le);
}

int main() {
  char str[40];
  scanf("%39s", str);
  double_ke(str);
  printf("%s\n",str );
  return 0;
}
