#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int len(char *str){
    int len = 0;
    while (str[len] != '\0'){
        len += 1;
    }
    return len;
}

int myfatoi(char *str){
    int n = len(str);
    int i;
    int res = 0;
    int ten_in_pow = 1;

    for (i = n - 1; i >= 0; i--){
        if (str[i] == '1'){
            res += 1*ten_in_pow;
            ten_in_pow *= 10;
        }
        if (str[i] == '2'){
            res += 2*ten_in_pow;
            ten_in_pow *= 10;
        }
        if (str[i] == '3'){
            res += 3*ten_in_pow;
            ten_in_pow *= 10;
        }
        if (str[i] == '4'){
            res += 4*ten_in_pow;
            ten_in_pow *= 10;
        }
        if (str[i] == '5'){
            res += 5*ten_in_pow;
            ten_in_pow *= 10;
        }
        if (str[i] == '6'){
            res += 6*ten_in_pow;
            ten_in_pow *= 10;
        }
        if (str[i] == '7'){
            res += 7*ten_in_pow;
            ten_in_pow *= 10;
        }
        if (str[i] == '8'){
            res += 8*ten_in_pow;
            ten_in_pow *= 10;
        }
        if (str[i] == '9'){
            res += 9*ten_in_pow;
            ten_in_pow *= 10;
        }
        if (str[i] == '0')
            ten_in_pow *= 10;
    }

    return res;
}
int fatoi (const char *str){
  return  atoi (str);
}
int main (void)
{
  char str[40];
  scanf("%39s", str);
  printf("%d + 1000 = %d \n",fatoi(str),fatoi(str)+ 1000);
  printf("%d + 1000 = %d \n",myfatoi(str),myfatoi(str)+ 1000);

   return 0;
}
