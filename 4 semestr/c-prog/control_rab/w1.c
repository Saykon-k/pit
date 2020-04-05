  #include "stdio.h"
  #include "math.h"
  double func(double alfa , double x){
    double res = (cos(alfa/2)*cos(alfa/2)+sin(alfa/2)*sin(alfa/2))/(cos(alfa/2)*cos(alfa/2))+x*x;
    return res;

  }
  int main(){
    double alfa;
    scanf("%f",&alfa);
    double prom1;
    double prom2;

    scanf("%f",&prom1);
    scanf("%f",&prom2);

    printf("%lf\n",func(prom1,prom2));

    double min =  func(alfa,-2.00) ;
    double prom;
    double x;
    for(x = -2.01 ; x <=2; x+= 0.01){
      prom = func(alfa,x);
      if(prom < min){
        min = prom;
      }
    }
    printf("%lf", min );
    return 0;
  }
