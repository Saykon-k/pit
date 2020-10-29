#include "stdio.h"
int main(){
  int x;
  int y;
  int count = 0;
  scanf("%d %d", &x,&y);
  int pow = 1;
  while(count < y){
    count++;
    pow *= x;
  }
  printf("%d", pow);
  return 0;
}
