
S = input("Nhập chuỗi: ")

tu = S.split()

da_xuat_hien = set()

ket_qua = None

for x in tu:
    if x in da_xuat_hien:
        ket_qua = x
        break
    da_xuat_hien.add(x)

print("Từ lặp đầu tiên là:", ket_qua)