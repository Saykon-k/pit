#include <stdio.h>
int main(){
    float x1, x2, x3;
    scanf("%f %f %f",&x1,&x2,&x3 );
    if(x1 > x2){
      if(x2 > x3 ){
        printf("%f\n", x3 );
      }else{
        printf("%f\n", x2 );
      }

    }else{
      if(x2 > x3){
        if( x3> x1 ){
          printf("%f", x1);
        }else{
          printf("%f", x3);
        }
      }else{
        printf("%f\n", x1 );
      }

    }
    return 0;
}
