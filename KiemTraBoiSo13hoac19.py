kiem_tra_boi = lambda n: n % 13 == 0 or n % 19 == 0

n = int(input("Nhập số nguyên n: "))
if kiem_tra_boi(n):
    print(f"{n} là bội số của 13 hoặc 19.")
else:
    print(f"{n} không phải là bội số của 13 hay 19.")