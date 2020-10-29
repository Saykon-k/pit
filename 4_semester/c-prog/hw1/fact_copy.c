#include <stdio.h>
double fact(double digit , double res){
  if (digit == 0 ){
    return res;
  }else{
    return fact(digit-1, res*digit);
  }
}
