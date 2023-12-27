def print_effect(n):
    step = 0
    for i in range(1, n + 1):
        print(' ' * (n+n-1),end="")
        # for j in range(1, i + 1):
        #     print(j, end=" ")
        line = " ".join(map(str, range(1, i +1)))
        print(line.ljust(n * 2 - 1), end='')
        print()

    for i in range(n+1, 1,-1):
        print(' '* step,end="")
        step+=1
        # for j in range(i-1, 0,-1):
        #     print(j, end="")
        line = " ".join(map(str, range(i-1, 0,-1)))
        print(line.center(n * 2 - 1),end='')
        print()





# Запрашиваем у пользователя число
num = int(input("Введите число: "))

# Создаем эффект
print_effect(num)







