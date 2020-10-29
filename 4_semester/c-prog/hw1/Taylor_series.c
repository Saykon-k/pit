#include <stdio.h>
#include "fact_copy.c"
double series_Taylor(int kolic){
  double e = 1;
  for(int i = 1; i<kolic+1; i++){
    e +=  1/fact(i,1);
  }
  return e;
}
int main(){
  int e;
  scanf("%d",&e );
  printf("%f digit ", series_Taylor(e) );
  return 0;
}
