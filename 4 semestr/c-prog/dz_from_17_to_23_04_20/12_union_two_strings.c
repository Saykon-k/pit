#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int findlen(char *str){
    int len = 0;
    while (str[len] != '\0'){
        len += 1;
    }
    return len;
}
void union_two_for_two(char *str, char *str2){
  int i = findlen(str);
  int i1 = findlen(str2);
  int n;
  for(n = 0 ; n < i1 ; n++){
    str[i+n] = str2[n];
  }
}
int main() {
  char str[40];
  scanf("%20s", str);
  char str2[40];
  scanf("%20s", str2);
  //char str[37] = "le", str2[54] = "go";
  printf("Let's union two line %s and %s \n", str,str2);
  union_two_for_two(str,str2);
  printf("%s\n",str );
  scanf("%20s", str);

  return 0;
}
