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
  int max_el = a[0],min_el = a[0];
  int index_max = 0 , index_min = 0;

  for(i = 1; i < N ; i++ ){
    if(max_el < a[i]){
      max_el = a[i];
      index_max = i;
    }
    if(a[i] < min_el) {
      min_el = a[i];
      index_min = i;
    }
  }
  printf("index_max %d index_min %d\n",index_max, index_min );
  min_el = 0;
  if(index_max>index_min){
    for(i = index_min+1; i < index_max; i++){
      min_el += a[i];
    }
  }else{
    for(i = index_max+1; i < index_min; i++){
      min_el += a[i];
    }
  }
  printf("sum = %d", min_el);
  return 0;
}
