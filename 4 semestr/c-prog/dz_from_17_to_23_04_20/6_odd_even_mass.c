#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "math.h"
#define N 10 /* количество элементов массива */
int mas_odd_even(int *mas,int chet,int odd_even){
  int i;
  for(i = odd_even; i < N ; i+=2){
    if( mas[i] % 2 == chet){
    }else{
      printf("%d a[%d] is not correct \n",mas[i],i);
      return -1;
      }
  }
  return 0;
}
int main()
{
  int a[N]; /* массив a размера N */
  int i;    /* счетчик */
  srand(time(NULL)); /* начальное значение генератора ПСЧ */
  for(i = 0; i < N; i++){
    a[i] = rand()%100;
    printf("%d , ", a[i]);
  }
  printf("\n");
  int chet = a[0] % 2 ;
  if(chet == 0){
  int proverk = mas_odd_even(a,0,2);
  if( proverk == 0 ){
    proverk = mas_odd_even(a,1,1);
    if(proverk == 0 ){
      printf("normas\n");
    }
  }
}else{
  int proverk = mas_odd_even(a,1,2);
  if( proverk == 0 ){
    proverk = mas_odd_even(a,0,1);
    if(proverk == 0 ){
      printf("normas\n");
    }
  }

}
  return 0;
}
