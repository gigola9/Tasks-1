for i in range(2, 1001):
    countOfDivision = 0
    for j in range(2, i + 1):
        if i % j == 0:
            countOfDivision += 1
    if countOfDivision == 1:
        print(i)


