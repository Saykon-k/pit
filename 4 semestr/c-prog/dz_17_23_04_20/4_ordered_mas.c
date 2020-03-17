#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "math.h"
#define N 10 /* количество элементов массива */

int main()
{
  int a[N]; /* массив a размера N */
  int i;    /* счетчик */
  srand(time(NULL)); /* начальное значение генератора ПСЧ */
  for(i = 0; i < N; i++){
    a[i] = rand()%100;
    printf("%d\n", a[i]);
  }
  for(i = 1; i < N; i++){
  if(a[i-1]> a[i]){
    printf("not ordered from min to max \n");
    return 1;
  }
}
  printf("not ordered from min to max \n" );
  return 0;
}
