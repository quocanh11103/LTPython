la_boi_13_hoac_19 = lambda n: n % 13 == 0 or n % 19 == 0

n = int(input("Nhập số nguyên n: "))
if la_boi_13_hoac_19(n):
    print(f"{n} là bội số của 13 hoặc 19.")
else:
    print(f"{n} không phải là bội số của 13 hoặc 19.")