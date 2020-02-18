#include "stdio.h"
float diam(float rad){
  return rad*2;
}
float per(float rad, float pi){
  return 2*pi*rad;
}
float area(float rad , float pi){
  return rad*rad*pi;
}
int main(){
  float rad;
  float pi  =  3.14159;
  scanf("%f", &rad);
  printf("%f - diam\n", diam(rad));
  printf("%f - per\n", per(rad, pi));
  printf("%f - area\n", area(rad,pi));
  return  0 ;
}
