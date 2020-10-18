#include "stdio.h"
#include "math.h"
void res(int *a , int *b){
  int c = *a;
  *a = *b;
  *b = c;


}
int main(){
  int a = 3  , b= 5  ;
  res(&a,&b);
  printf("%d\n", a);
  printf("%d\n", b);
  scanf("%d",a);
  return 0;
}
