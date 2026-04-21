n = int(input("Nhập số nguyên dương n: "))
soln = 0

while n > 0:
    chuso = n % 10
    if chuso > soln:
        soln = chuso
    n = n // 10

print("Số lớn nhất:", soln)