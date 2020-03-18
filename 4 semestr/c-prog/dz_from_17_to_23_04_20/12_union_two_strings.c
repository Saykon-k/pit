#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//все равно неправильно.
void union_two(char *str, char *str2){

  //если поставить i вместо 100 не заработает ,почему?
  strcat(str,str2);
}
int main() {
  char str[37] = "ser", str2[54] = "gay";
  printf("Let's union two line %s and %s \n", str,str2);
  union_two(str,str2);
  printf("%s\n",str );
  return 0;
}
