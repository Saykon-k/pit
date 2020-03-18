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
  // for(i = 0; i < N/2; i++){
  //   a[i] = i;
  // }
  // for(i = (int) N/2; i < N ; i++){
  //   a[i] = (sizeof(a)/4)-i-1;
  // } this code for generate mass-polindom
  for(i = 0; i < N; i++){
    a[i] = rand()%100;
    printf("%d , ", a[i]);
  }
  printf("\n");
  int half_len_mas = (int) sizeof(a)/4-1;
  if(N  % 2 == 0){
    for(i = 0; i < half_len_mas/2 ; i++ ){
      //printf("a[i] == %d a[half_len_mas-i] == %d\n", a[i],a[half_len_mas-i]);
    if(a[i] != a[half_len_mas-i]){
      printf("a[i] == %d  != a[half_len_mas-i]  == %d\n", a[i],a[half_len_mas-i]);
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
