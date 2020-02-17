#include "stdio.h"
int main() {
  int all;
  scanf("%d", &all);

  int s[all];
  all = 0;
  for(int i = 0; i < sizeof(s)/4 ;i++){
    scanf("%d",&s[i] );
    all += s[i];
    }
  printf("%d", all);
  return 0;
}
