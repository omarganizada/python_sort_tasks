import random
def lenn(massiv):
    s = 0
    for i in massiv:
        s += 1
    return s
def sum_digits(x):
    s = 0
    while x:
        s += x%10
        x = x//10
    return s
def bubble_sort_by_digits(x):
    x_len = lenn(x)
    for i in range(x_len):
        for j in range(x_len - i - 1):
            if sum_digits(x[j]) < sum_digits(x[j + 1]):
                x[j] , x[j + 1] = x[j + 1] , x[j]
    return x
massiv =[random.randint(0,1000) for i in range(5) ]
print(massiv)
print(bubble_sort_by_digits(massiv))
