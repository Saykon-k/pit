#include "stdio.h"
int main() {
  double kolic;
  printf("Write value ");
  scanf("%lf", &kolic);
  double product = 1;
  for(int i = 1 ; i <= kolic ; i+=2 ){
    product *= i;
  }
  printf("%lf" , product);
  return 0;
}
