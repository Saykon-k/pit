#include "stdio.h"
int main(){
  int kol;
  printf("Write number of sequence ");
  scanf("%d", &kol);
  double two_elemnt[2];
  double max[kol];

  scanf("%lf", &max[0]);
  scanf("%lf", &max[1]);
  two_elemnt[0] = max[0];
  two_elemnt[1] = max[1];

  if(two_elemnt[0] > two_elemnt[1]){
    two_elemnt[1] += two_elemnt[0];
    two_elemnt[0] = two_elemnt[1] - two_elemnt[0];
    two_elemnt[1] -= two_elemnt[0];
  }

  for(int i = 2; i < kol ; i++){
     scanf("%lf", &max[i]);
     if(max[i]<two_elemnt[0]){
       two_elemnt[0] = max[i];
     }else{
       if(max[i] > two_elemnt[1]) two_elemnt[1] = max[i];
     }
}
  printf("%lf %lf ", two_elemnt[0], two_elemnt[1]);
  return 0;
}
