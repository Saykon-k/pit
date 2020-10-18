#include "stdio.h"
int main(){
  int count = 0;
  int sum = 0;
  while(count<10){
    count++;
    sum += count;
  }
  printf("%d\n",sum );
}
