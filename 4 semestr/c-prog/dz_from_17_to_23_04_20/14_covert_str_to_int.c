#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int fatoi (const char *str){
  return  atoi (str);
}
int main (void)
{
  char str[40];
  scanf("%39s", str);
  printf("%d + 1000 = %d \n",fatoi(str),fatoi(str)+ 1000);
   return 0;
}
