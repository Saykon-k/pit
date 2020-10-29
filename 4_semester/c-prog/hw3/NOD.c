
#include <stdio.h>
double min(double a, double b)
{
    while(a!= 0 && b != 0 ){
      if (a>b){
        a = a - b;
      }else{
        b = b - a;
      }
    }
    return a+b;
}

int main()
{
        double a, b;
        double res;

        printf("Enter numbers: ");
        scanf("%lf %lf", &a, &b);

        res = min(a, b);

        printf("Minimum is %f\n", res);

        return 0;
}
