class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return 'Error: Division by zero'
        return a / b

def main():
    calculator = Calculator()
    while True:
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        print('5. Quit')
        try:
            choice = input('Choose an operation (1/2/3/4/5): ')
            if choice in ['1', '2', '3', '4']:
                try:
                    num1 = float(input('Enter first number: '))
                    num2 = float(input('Enter second number: '))
                    if choice == '1':
                        print(f'{num1} + {num2} = {calculator.add(num1, num2)}')
                    elif choice == '2':
                        print(f'{num1} - {num2} = {calculator.subtract(num1, num2)}')
                    elif choice == '3':
                        print(f'{num1} * {num2} = {calculator.multiply(num1, num2)}')
                    elif choice == '4':
                        print(f'{num1} / {num2} = {calculator.divide(num1, num2)}')
                except ValueError:
                    print('Invalid input. Please enter a number.')
            elif choice == '5':
                print('Goodbye!')
                break
            else:
                print('Invalid choice. Please choose a valid operation.')
        except EOFError:
            print('Invalid input. Please enter a choice.')
if __name__ == '__main__':
    main()