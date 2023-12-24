#include <stdio.h>

int print(int m);

int main() 
{
    int a, b;
    scanf("%d %d", &a, &b);

    for (int i = a; i <= b; i++) {
        print(i);
    }

    return 0;
}

int print(int m) {
    if (m == 1) {
        printf("one\n");
    } else if (m == 2) {
        printf("two\n");
    } else if (m == 3) {
        printf("three\n");
    } else if (m == 4) {
        printf("four\n");
    } else if (m == 5) {
        printf("five\n");
    } else if (m == 6) {
        printf("six\n");
    } else if (m == 7) {
        printf("seven\n");
    } else if (m == 8) {
        printf("eight\n");
    } else if (m == 9) {
        printf("nine\n");
    } else if (m % 2 == 0) {
        printf("even\n");
    } else {
        printf("odd\n");
    }

    return 0;
}
