#include "stdio.h"
long long int  fact(int digit , int res){
  if (digit == 0 ){
    return res;
  }else{
    return fact(digit-1, res*digit);
  }
}
int main(){
  int number;
  printf("Write a number: ");
  scanf("%d", &number );
  printf("%d - your resault \n",fact(number,1));
  return 0;
}
