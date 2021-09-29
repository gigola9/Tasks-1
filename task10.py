print("შეიყვანეთ წელი")
num = int(input())

if (num % 4 == 0 and num % 100 != 00) or (num % 100 == 0 and num % 400 == 0):
    print("ნაკიანია")
else:
    print("არ არის ნაკიანი")