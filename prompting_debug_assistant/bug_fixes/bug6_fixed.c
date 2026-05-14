#include <stdio.h>

int factorial(int n) {
    int result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

void print_table(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            printf("%4d", i * j);
        }
        printf("\n");
    }
}

int main() {
    printf("Factorial of 5: %d\n", factorial(5));
    printf("Factorial of 1: %d\n", factorial(1));
    printf("\nMultiplication table (3x3):\n");
    print_table(3);
    return 0;
}
