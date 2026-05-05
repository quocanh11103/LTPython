def luy_thua(a, b):
    if b == 0:
        return 1

    return a * luy_thua(a, b - 1)


a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

print(a, "^", b, "=", luy_thua(a, b))
