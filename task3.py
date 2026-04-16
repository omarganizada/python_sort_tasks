def lenn(x):
    s = 0
    for i in x:
        s += 1
    return s
def bubble_sort(x):
    len_x = lenn(x)
    for i in range(len_x):
        for j in range(len_x - i - 1):
            if x[j] > x[j+1]:
                x[j] , x[j + 1] = x[j+1] , x[j]
    return x
massiv = []
print("Sozleri daxil edin")
for i in range(1, 6):
    massiv += [input(f"{i}. ")]
print(bubble_sort(massiv))
