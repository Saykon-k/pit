#include <conio.h>
#include <stdio.h>

void main() {
  // string variable
char str[6] = "Hello";

// pointer variable
char *ptr = str;

// print the string
while(*ptr != '\0') {
  printf("%p ", ptr);

  // move the ptr pointer to the next memory location
  ptr++;
}
  return 0;
}
