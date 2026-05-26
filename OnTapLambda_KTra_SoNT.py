la_so_nguyen_to = lambda n: n >= 2 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

n = int(input("Nhập số nguyên n: "))
if la_so_nguyen_to(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")