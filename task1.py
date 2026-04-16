import random
def lenn(massiv):
    s = 0
    for i in massiv:
        s += 1
    return s
def check(massiv,axtarilan):
    for i in massiv:
        if i == axtarilan:
            return True
    return False
massiv =[random.randint(0,6) for i in range(5) ]
axtarilan = int(input("Axtarilan ededi daxil et:"))
print("Massiv:")
print(massiv)
print("Ne axtaririq:",axtarilan)
if check(massiv,axtarilan):
    print("Tapildi: ",end = "")
else:
    print("Tapilmadi.")
for i in range(lenn(massiv)):
    if massiv[i] == axtarilan:
        print(f"A[{i+1}]={axtarilan}",end = " ")
