#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "math.h"
void fild_z(int *z,int len){
  int i = 0;
  for(i = 0; i < len ; i++){
    z[i] = 0;
  }
}
int main()
{
  int size_mas_a , size_mas_b;
  scanf("%d", &size_mas_a);
  scanf("%d", &size_mas_b);
  int a[size_mas_a];
  int  b[size_mas_b]; /* массив a размера N */
  int i,i1;    /* счетчик */
  srand(time(NULL));
  for(i = 0; i < size_mas_a; i++){
    a[i] = rand()%100;
    printf("%d ", a[i]);
  }
  printf("\n");
  for(i = 0; i < size_mas_b; i++){
    b[i] = rand()%100;
    printf("%d ", b[i]);
  }
  printf("\n");
  if(sizeof(a)>sizeof(b)){
    int z[size_mas_b];
    fild_z(z , size_mas_b);
    for(i = 0; i < sizeof(a)/4 ; i++ ){
      for(i1 = 0 ; i1 < sizeof(b)/4; i1++){
        if(a[i] == b[i1]){
          z[i1] = a[i];
          printf("%d \n",a[i]);
          i1 = sizeof(b)/4;
        }
      }
    }
    for(i = 0 ; i<size_mas_b;i++){
      if(z[i]!=0){
        printf("%d ",z[i] );
      }
    }
  }else{
    int z[size_mas_a];
    fild_z(z , size_mas_b);
    for(i = 0; i < sizeof(a)/4 ; i++ ){

      for(i1 = 0 ; i1 < sizeof(b)/4; i1++){
        if(a[i] == b[i1]){
          z[i1] = a[i];
          printf("%d\n",a[i]);
          i1 = sizeof(b)/4;
        }
      }

    }
    for(i = 0 ; i<size_mas_b;i++){
      if(z[i]!=0){
        printf("%d ",z[i] );
      }
    }
  }

  return 0;
}
