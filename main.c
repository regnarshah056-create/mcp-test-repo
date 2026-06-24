#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to add two numbers
float add(float a, float b) {
    return a + b;
}

// Function to subtract two numbers
float subtract(float a, float b) {
    return a - b;
}

// Function to multiply two numbers
float multiply(float a, float b) {
    return a * b;
}

// Function to divide two numbers
float divide(float a, float b) {
    if (b == 0) {
        printf("Error: Division by zero\n");
        return NAN; // Return Not a Number instead of exiting
    }
    return a / b;
}

int main() {
    float num1, num2;
    char operation;
    printf("Enter the first number: ");
    scanf("%f", &num1);
    printf("Enter the second number: ");
    scanf("%f", &num2);
    printf("Enter the operation (+, -, *, /): ");
    scanf(" %c", &operation);
    switch (operation) {
        case '+':
            printf("Result: %f\n", add(num1, num2));
            break;
        case '-':
            printf("Result: %f\n", subtract(num1, num2));
            break;
        case '*':
            printf("Result: %f\n", multiply(num1, num2));
            break;
        case '/':
            {
                float result = divide(num1, num2);
                if (isnan(result)) {
                    printf("Error: Division by zero\n");
                } else {
                    printf("Result: %f\n", result);
                }
            }
            break;
        default:
            printf("Invalid operation\n");
    }
    return 0;
}