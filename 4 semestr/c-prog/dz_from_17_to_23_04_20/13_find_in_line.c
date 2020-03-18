#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int  find_in_line(char *str, char word){
  int i ;
  for( i = 0 ;str[i] != '\0'; i++){
    if(str[i] == word ){
      return  *str[i];
    }
  }
  return -1;
}
int main() {
  char str[37] = "er";
  char  word  = "s";
  printf("%d\n",find_in_line(str,word));

  return 0;
}
