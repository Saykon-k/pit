#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "math.h"
#define N 10 /* количество элементов массива */
//задание найти уникальные элементы в массиве а и записать их в массив б
//1.создаем псевдослучайные действительные числа
//2.создаем массив длинной сравнимым с иходным.Потом берем каждое число из массива а и сравниваем до того момента,
//пока что не найдем повтор,если повтор находится, то данный элемент не заносится в новый список
//длинна массива массива б также считается в нем
//после делается стандартная сортировка пузырьком и вывод результа
int main()
{
  double a[N]; /* массив a размера N */
  int i,i1;    /* счетчик */
  int prom;
  srand(time(NULL)); /* начальное значение генератора ПСЧ */
  //1.
  for(i = 0; i < N; i++){
    a[i] = rand()%5 ;
    prom = rand()%2;
     a[i] += 0.1*prom;
    printf("%lf index %d\n", a[i],i);
  }
  //2.
  int b_len = 0 ;
  double prom_b[N];
  int povtor = 0;
  int real_b_len = 0;
  for(i = 0; i < N; i++){
    for(i1 = 0; i1 < N; i1++){
      if(a[i] == prom_b[i1]){
        povtor = 1;
         i1 = N;
      }
    }
    if(povtor == 0){
      prom_b[b_len] = a[i];
      real_b_len++;
      b_len++;
    }else{
      prom_b[b_len] = -1;
      b_len++;
    }
    povtor = 0;
  }
    printf("%d- size  mas b\n",real_b_len );
    double real_b[real_b_len];
    real_b_len = 0;
    for(i = 0 ; i<N ; i++){
    if(prom_b[i]!=-1){
      real_b[real_b_len] = prom_b[i];
      real_b_len++;
    }
    printf("\n");
  }
  for(i = 0 ; i < real_b_len ; i++){
    printf("%lf ", real_b[i] );
  }
  printf("\n");
  double prom_2;
  for(i = 0; i< real_b_len; i++){
    for(i1 = 0; i1<real_b_len; i1++){
      //printf("%lf index %d  %lf %d  \n" , real_b[i],i,real_b[i1],i1);
        if(real_b[i]< real_b[i1]){
        prom_2 = real_b[i];
        real_b[i] = real_b[i1];
        real_b[i1] = prom_2;
      }
    }
  }
  for(i = 0 ; i < real_b_len ; i++){
    printf("%lf ", real_b[i] );
  }
    return 0;
}
