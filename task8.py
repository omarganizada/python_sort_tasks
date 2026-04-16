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
def binary_search(A, target):
   left = 0
   right = len(A) - 1
   count = 0
   while left <= right:
       mid = (left + right) // 2
       count += 1
       if target == A[mid]:
           return mid, count
       else:
           if target > A[mid]:
               left = mid + 1
           else:
               right = mid - 1
   return -1
a = [random.randint(1, 11) for i in range(9)]
print("Massiv:",a)
print("Cesidlemeden sonra:",bubble_sort(a))
x = int(input("X ededi daxil edin:"))
if binary_search(a,x) == -1:
    print("Tapilmadi")
else:
    print(f"Tapildi. A[{binary_search(a,x)[0]}] = {x}")
    print(f"Muqayise sayi: {binary_search(a,x)[1]}")
