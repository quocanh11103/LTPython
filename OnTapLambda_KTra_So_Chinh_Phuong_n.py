import math

la_so_chinh_phuong = lambda n: n >= 0 and int(math.isqrt(n)) ** 2 == n

n = int(input("Nhập số nguyên n: "))
if la_so_chinh_phuong(n):
    print(f"{n} là số chính phương (căn bậc hai = {int(math.isqrt(n))}).")
else:
    print(f"{n} không phải là số chính phương.")