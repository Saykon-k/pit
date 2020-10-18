#include "stdio.h"
int main(){
  int kol;
  int minim;
  printf("Write number of sequence ");
  scanf("%d", &kol);

  int max[kol];
  scanf("%d", &max[0]);
  if(max[0] > 0){
    minim = max[0];
  }else{
  minim = 0;
  }
  for(int i = 1; i < kol ; i++){
    scanf("%d", &max[i]);
    if(max[i] > 0  && max[i] < minim ){
      minim = max[i];
    }
  }
  printf("minimum is %d", minim);
  return 0;
}
