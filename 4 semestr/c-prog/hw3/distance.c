#include "stdio.h"
#include "math.h"
int main() {
  float y1,x2,y2;
  int x1;
  scanf("%f" ,&x1);
  scanf("%f" ,&y1);
  scanf("%f" ,&x2);
  scanf("%f" ,&y2);
  printf("%f",sqrt(pow((x2-x1),2)+pow((y2-y1),2)));
  return 0;
}
