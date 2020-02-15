#include <stdio.h>

int main()
{
   int chiclo, frs, sec, l_frs, l_sec;

   scanf("%d",&chiclo );
юс   frs = chiclo/10000;
   l_frs = chiclo%10;
   sec = chiclo/ 1000 % 10;
   l_sec = chiclo % 100 /10;
   if(frs == l_frs && sec == l_sec ){
     printf("palindrome");
 }else{
   printf("not the palindrome");
 }
   return 0;
}
