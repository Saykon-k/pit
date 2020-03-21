#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void union_two_for_two(char *str, char *str2){
  strcat(str,str2);
}
int main() {
  char str[40];
  scanf("%39s", str);
  char str2[40];
  scanf("%39s", str2);
  //char str[37] = "le", str2[54] = "go";
  printf("Let's union two line %s and %s \n", str,str2);
  union_two_for_two(str,str2);
  printf("%s\n",str );
  return 0;
}
