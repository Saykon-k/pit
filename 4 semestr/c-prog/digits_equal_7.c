#include "stdio.h"
int main(){
  int chiclo;
  int counter = 0 ;
  scanf("%d",&chiclo);
  while(chiclo>0){
    if(chiclo % 10 == 7){
      counter++;
    }
    chiclo /= 10;
  }
  printf("%d\n", counter);
  return 0;
}
