#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "math.h"
#define N 3 /* количество элементов массива */

int main()
{
  int a[N]; /* массив a размера N */
  int i;    /* счетчик */
  srand(time(NULL)); /* начальное значение генератора ПСЧ */
  for(i = 0; i < N/2; i++){
    a[i] = i;
  }
  a[1] = 1;
  a[2] = 0;
  int half_len_mas = sizeof(N)/4;
  if(N  % 2 == 0){
    for(i = 0; i < half_len_mas/2 ; i++ ){
      printf("%d\n", a[i] != a[half_len_mas-i]);
    if(a[i] != a[half_len_mas-i]){
      printf("ne polindrom\n");
      i = half_len_mas;
    }
  }

}else {
  for(i = 0; i < half_len_mas/2 ; i++ ){
    if(a[i] != a[half_len_mas-i]){
      printf("ne polindom\n");
      i = half_len_mas;
    }
  }
}

  return 0;
}
