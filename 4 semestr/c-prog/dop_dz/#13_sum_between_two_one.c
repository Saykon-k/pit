#include "stdio.h"
int main(){
  int kol;
  printf("Write number of sequence ");
  scanf("%d", &kol);
  double max[kol];
  int element[2] = {-1,-1};
  int t = 0;
  for(int i = 0; i < kol ; i++){
     scanf("%lf", &max[i]);
     if(t == 0 && max[i] == 1){
       element[0] = i;
       t++;
     }else{
       if(max[i] == 1) element[1] = i;
     }
}
  if(element[0] == -1 && element[1] == -1){
    printf("the borders is not find");
    return 1;
  }else{
    if(element[1] == -1 ){
      printf("second borders is not find");
      return 1;
    }else{
      printf("first borders is not find");
      return 1;
    }
  }

  double sum = 0;
  for(int i = element[0]; i <=element[1]; i++){
    sum+=max[i];
  }
  printf("%lf\n", sum );
  return 0;
}
