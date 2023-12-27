def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# number = 5
# result_recursive = fibonacci_recursive(number)
# print(f"Рекурсивное число Фибоначчи для {number}: {result_recursive}")


def fibonacci_iterative(n):
    if n <= 1:
        return n

    fibonacci = [0, 1]
    for i in range(2, n + 1):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

    return fibonacci[n]


# number = 10
# result_iterative = fibonacci_iterative(number)
# print(f"Итеративное число Фибоначчи для {number}: {result_iterative}")



def fibonacci_iterative_large(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        print (a,b)

    return b % 10  

number_large = 11151
result_iterative_large = fibonacci_iterative_large(number_large)
print(f"Последняя цифра числа Фибоначчи для {number_large}: {result_iterative_large}")
