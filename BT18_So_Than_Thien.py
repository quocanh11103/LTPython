# a_so_than_thien.py
import math

so_than_thien = lambda n: math.gcd(n, int(str(n)[::-1])) == 1

print("Các số THÂN THIỆN từ 1 đến 1 triệu:")
ket_qua = [n for n in range(1, 1_000_001) if so_than_thien(n)]
print(f"Tổng số: {len(ket_qua)}")
print(f"10 số đầu: {ket_qua[:10]}")