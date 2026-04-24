import math
# Kiểm tra n có lớn hơn 1 và không chia hết cho số nào từ 2 đến căn n
la_so_nguyen_to = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

n = int(input("Nhập số nguyên n: "))
if la_so_nguyen_to(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")