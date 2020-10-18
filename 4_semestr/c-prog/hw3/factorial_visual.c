
#include <stdio.h>

long int factorial(int number, long int result)
{
if (number == 0)
{
    return result;
}
else{
    printf("%ld!\n",  result);
    return factorial(number - 1, result*number);
}
}

int main()
{
int number;

number = 0;

printf("Enter number: ");
scanf("%d", &number);

factorial(number, 1);

return 0;
}
