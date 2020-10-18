#include <stdio.h>
#include <stdbool.h>
bool isPrime(int n){
    if (n > 1)
    {
        for (int i = 2; i < n; i++)
            if (n % i == 0)
                return false;


        return true;
    }
    else
        return false;
}
int main()
{
    int n;

    printf("Input a number: ");

    scanf_s("%d", &n);

    printf("Is prime: %d\n", isPrime(n));
}
