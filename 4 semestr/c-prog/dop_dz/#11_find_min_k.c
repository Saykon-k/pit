#include "stdio.h"
int main(){
  double k;
  int kol;
  double minim;
  int numer;
  printf("Write k ");
  scanf("%lf", &k );

  printf("Write number of sequence ");
  scanf("%d", &kol);

  double max[kol];

  for(int i = 0; i < kol ; i++){
     scanf("%lf", &max[i]);
     if(max[i]>k){
       numer = i;
     }
}

  printf("numer is %d", numer+1);
  return 0;
}
