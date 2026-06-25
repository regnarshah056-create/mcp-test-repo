#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    return a * b;
}

int divide(int a, int b) {
    if (b == 0) {
        throw runtime_error("Division by zero");
    }
    return a / b;
}

int main() {
    int choice, num1, num2;
    while (true) {
        cout << "1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n";
        cout << "Enter your choice: ";
        cin >> choice;
        if (choice >= 1 && choice <= 4) {
            break;
        }
        cout << "Invalid choice. Please choose a valid option.\n";
    }
    cout << "Enter first number: ";
    cin >> num1;
    cout << "Enter second number: ";
    cin >> num2;

    switch (choice) {
        case 1:
            cout << num1 << " + " << num2 << " = " << add(num1, num2);
            break;
        case 2:
            cout << num1 << " - " << num2 << " = " << subtract(num1, num2);
            break;
        case 3:
            cout << num1 << " * " << num2 << " = " << multiply(num1, num2);
            break;
        case 4:
            try {
                cout << num1 << " / " << num2 << " = " << divide(num1, num2);
            } catch (const exception& e) {
                cerr << e.what() << "\n";
            }
            break;
    }

    return 0;
}