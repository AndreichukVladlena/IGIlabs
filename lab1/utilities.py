def hello_world():
    print("Hello world!")


def operation(num1, num2, op):
    if op == "add":
        return num1 + num2
    elif op == "sub":
        return num1 - num2
    elif op == "mult":
        return num1 * num2
    elif op == "div":
        return num1 * num2
    else:
        return 0


def save_even_numbers():
    numbers = [5, 6, 7, 3, 2, 1, 9, 4555, 2, 2, 21, 23]
    new_numbers = []
    for n in numbers:
        if n % 2 == 0:
            new_numbers.append(n)
    return new_numbers
