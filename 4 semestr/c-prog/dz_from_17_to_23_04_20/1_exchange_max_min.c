#include <stdio.h>
#include <stdlib.h>
#include <time.h>
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
  int max_el = a[0];
  int min_el = a[0];
  int index_max = 0;
  int index_min = 0;
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
 a[index_max] = min_el;
 a[index_min] = max_el;
 printf("max = %d  min = %d \n", a[index_max] , a[index_min] );
 for(i = 0; i < N; i++){
   printf("%d\n", a[i]);
 }
  return 0;
}
