#include "stdio.h"
int main(){
  int kol;
  printf("Write number of sequence ");
  scanf("%d", &kol);
  double max_element;
  double max[kol];
  double numer = 1 ;

  scanf("%lf", &max[0]);
  max_element = max[0];

  for(int i = 1; i < kol ; i++){
    
     scanf("%lf", &max[i]);
     if(max_element<max[i]){
        max_element = max[i];
        numer = i+1;
}
}
  printf("%lf ", sizeof(max)/8 - numer);
  return 0;
}
