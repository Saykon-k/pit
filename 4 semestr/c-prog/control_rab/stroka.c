#include "stdio.h"
#include "math.h"
int len(char *s){
  int i = 0 ;
  while(s[i] != '\0'){
    i++;
  }
  return i;
}
int main(){
  char s[14];
  printf("%d\n", len(s) );
  printf("%d\n",sizeof(s)-1);
  return 0;
}
