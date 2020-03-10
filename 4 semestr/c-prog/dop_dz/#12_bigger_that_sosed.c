#include "stdio.h"
int main(){
  int kol_minimu = 0 ;
  int kol;
  int minim;
  printf("Write number of sequence ");
  scanf("%d", &kol);

  int max[kol];
  int kol_minimum_mas[kol];
  for(int i = 0; i < kol ; i++){
    kol_minimum_mas[i] = -1;
}

  for(int i = 0; i < kol ; i++){
    scanf("%d", &max[i]);
  }

  for(int i = 0; i < kol-1 ; i++){
  if(max[i] > max[i+1]){
    kol_minimum_mas[i] = i;
    kol_minimu++;
  }
}
printf("numer of element ");
  for(int i = 0; i < kol-1 ; i++){
    if(kol_minimum_mas[i] != -1){
    printf("%d ", kol_minimum_mas[i]+1);
  }
}
  printf("\nkol  bigger that right sosed is %d", kol_minimu);
  return 0;
}
