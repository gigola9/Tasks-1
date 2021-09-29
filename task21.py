print("შეიყვანეთ პირველი რიცხვი")
first = int(input())
print("შეიყვანეთ მეორე რიცხვი")
second = int(input())
res = 1

for i in range(1, first + 1):
    if second % i == 0 and first % i == 0:
        res = i

print(res)
