import math

dien_tich_hinh_tron = lambda r: math.pi * r ** 2

r = float(input("Nhập bán kính r: "))
print(f"Diện tích hình tròn bán kính {r} = {dien_tich_hinh_tron(r):.4f}")