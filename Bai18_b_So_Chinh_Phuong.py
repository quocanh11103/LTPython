# b_so_chinh_phuong.py
import math

so_chinh_phuong = lambda n: math.isqrt(n) ** 2 == n

print("Các số CHÍNH PHƯƠNG từ 1 đến 1 triệu:")
ket_qua = [n for n in range(1, 1_000_001) if so_chinh_phuong(n)]
print(ket_qua)