# TODO
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

summa_kvadratov = a**2+b**2
kv_summa = (a+b)**2
print(summa_kvadratov, kv_summa)
if summa_kvadratov>kv_summa:
    print("Сумма квадратов больше")
elif summa_kvadratov<kv_summa:
    print("Квадрат суммы больше")
else:
    print("Равны")