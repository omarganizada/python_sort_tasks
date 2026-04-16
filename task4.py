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
print("Ad, ata adı və soyadınizi daxil edin:")
massiv = []
x = input()
while x != "":
    massiv = massiv + [x]
    x = input()
print(bubble_sort(massiv))
