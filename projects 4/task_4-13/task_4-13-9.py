array = [5, 3, 8, 4, 2, 7, 1]
E = 0
for i in array:
    if i % 2 != 0:
        E = i + E

print("Сумма всех нечетных элементов массива:", E)
