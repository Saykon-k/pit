#include "stdio.h"
int main() {
  int all;
  scanf("%d", &all);
  int counter = 0 ;
  int sum = 0;
  while(all != 9999){
  scanf("%d", &all);
  sum += all;
  counter++;
  }
  printf("%d" , sum/counter);
  return 0;
}
