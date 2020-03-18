#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void double_ke(char *s){
  int i = 0 ;
  while(s[i] != '\0'){
    i++;
  }
  //если поставить i вместо 100 не заработает ,почему?
  char le[100] = "";
  strcat(le,s);
  strcat(s,le);
}
int main() {
  char str[37] = "sergey";
  // strcat(s,str);
  // strcat(str,s);
  // printf("%s\n",str );
  double_ke(str);
  printf("%s\n",str );
  return 0;
}
