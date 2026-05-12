def doi_tien(so_tien):
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    so_to = {}
    con_lai = so_tien

    for tien in menh_gia:
        so_to[tien] = con_lai // tien
        con_lai %= tien

    return so_to

def in_ket_qua(X, so_to):
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    print(f"So tien {X} duoc doi thanh:")
    
    tong = 0
    so_loai = 0
    
    for tien in menh_gia:
        if so_to[tien] > 0:          # Chỉ in loại tiền có số tờ > 0
            print(f"Loai {tien} gom {so_to[tien]} to")
            tong += so_to[tien]
            so_loai += 1
    
    print(f"TONG CONG CO {tong} TO")
    print(f"Tong so loai = {so_loai}")


# ========== CHƯƠNG TRÌNH MỞ RỘNG ==========
a = int(input("Nhap so tien hang can phai tra (a): "))
b = int(input("Nhap so tien khach hang dua (b): "))

if a > b:
    print(f"Khach hang con thieu: {a - b}")

elif a == b:
    print("Cam on khach hang. Hen gap lai!")

else:  # a < b: cần thối tiền
    tien_thoi = b - a
    so_to = doi_tien(tien_thoi)
    
    print(f"\nCan thoi lai cho khach: {tien_thoi}")
    in_ket_qua(tien_thoi, so_to)
    
    input("\nNhan Enter de ket thuc...")
    print("Cam on khach hang. Hen gap lai!")