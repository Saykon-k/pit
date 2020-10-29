#include "stdio.h"
int main() {
  int kolic;
  int pred;
  int min;

  printf("Write number of digits ");
  scanf("%d", &kolic);
  printf("Write value ");
  scanf("%d", &pred);

  min = pred;
  while(kolic != 1){

    printf("Write value ");
    scanf("%d", &pred);

    if(pred < min){
      min = pred;
    }
    kolic--;
  }
  printf("%d", min);
  return 0;
}
