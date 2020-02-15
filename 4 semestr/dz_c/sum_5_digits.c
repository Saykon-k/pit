#include "stdio.h"
int main() {
  int s[] = {0,0,0,0,0};
  int all = 0 ;
  for(int i = 0; i<5 ;i++){
    scanf("%d",&s[i] );
    all += s[i];
    }
  printf("%d", all/(sizeof(s)/4));
  return 0;
}
