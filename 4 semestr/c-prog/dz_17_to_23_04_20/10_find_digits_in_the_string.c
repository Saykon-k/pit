#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "math.h"
#define N 10 /* количество элементов массива */
int kol_digits_in_str(char *str , int len){
  int i;
  int kol = 0;
  for(i = 0; i<len; i++){
    if(str[i] == '0' || str[i] == '1' || str[i] == '2' ||
      str[i] == '3' || str[i] == '4' || str[i] == '5' ||
      str[i] == '6' || str[i] == '7' || str[i] == '8' ||
      str[i] == '9'){
        kol++;
    }
  }
  return kol;
}
int main()
{
  char str[40];
  scanf("%39s", str);
  printf("%d", kol_digits_in_str(str,sizeof(str)));
  return 0;
}
