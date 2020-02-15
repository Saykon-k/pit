#include <stdio.h>
#include <math.h>
#include "fact_copy.c"
double series_Taylor(int kolic,double x ){
  double e = 1;
  double stip =1 ;
  for(double i = 1; i<kolic+1; i++){
    stip = pow(x, i);
    e += stip/fact(i,1);
  }
  return e;
}
int main(){
  int kolic;
  float x;

  printf("Write number of members:");
  scanf("%d", &kolic);

  printf("Write power for E:");
  scanf("%f", &x);

  printf("%f\n",series_Taylor(kolic,x));
}
