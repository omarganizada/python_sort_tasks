import random
def bubble_sort(x):
    len_x = lenn(x)
    for i in range(len_x):
        for j in range(len_x - i - 1):
            if x[j] > x[j+1]:
                x[j] , x[j + 1] = x[j+1] , x[j]
    return x
def lenn(x):
    l = 0
    for i in x:
        l += 1
    return l
unsorted_massiv = [random.randint(-100,101) for i in range(10)]
sorted_1 = bubble_sort(unsorted_massiv)
sorted_2 = sorted_1[4::-1] + sorted_1[:4:-1] 
print(unsorted_massiv)
print(sorted_1)
print(sorted_2)
