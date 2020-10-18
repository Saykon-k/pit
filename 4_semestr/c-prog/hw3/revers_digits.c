#include<stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
  int num;
  scanf("%d",&num );
  char snum[50];
  itoa(num, snum, 10);
  printf("\nYour reverse string is: %s",strrev(snum));
  return(0);
}
