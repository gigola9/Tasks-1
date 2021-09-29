def task2(num):
    if num == 0:
        return 0
    else:
        return num % 2 + (10 * task2(num // 2))


print("შეიყვანეთ რიცხვი: ")
decimal = input()
print(task2(int(decimal)))
