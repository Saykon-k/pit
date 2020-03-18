#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int fatoi (const char *Str){
  return  atoi (Str);
}
int main (void)
{
   char *Str = "556"; 
   printf("%d\n",atoi(Str));
   return 0;
}
