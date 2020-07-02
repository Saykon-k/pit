#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
struct data{
  int day_gey;
  char *mouth;
  int year;
};
int main(){
  struct data d={8,"ortor", 1978};
  printf("%d %s %d \n", d.day_gey,d.mouth,d.year);
  return 0;
}
