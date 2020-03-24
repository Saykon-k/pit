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
  double r;
  scanf("%lf", &r);
  for(i = 0; i < N; i++){
    a[i] = rand()%100;
    printf("%d\n", a[i]);
  }
  double prom = -1, rad_min = labs(a[0] - r) ;
  int el = 0;
  printf("rad el = %lf\n", rad_min );
  for(i = 1 ; i < N; i++){
    prom = labs(r - a[i]);
    if(prom < rad_min){
     rad_min = prom;
     el = i;
    }

  }
  printf("closerst_el = %d \n", a[el] ,  );
  return 0;
}
