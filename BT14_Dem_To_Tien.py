X = int(input("Nhap so tien X: "))

menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]

so_to = {}
con_lai = X

for tien in menh_gia:
    so_to[tien] = con_lai // tien
    con_lai %= tien

print(f"So tien {X} duoc doi thanh:")
tong = 0
for tien in menh_gia:
    print(f"Loai {tien} gom {so_to[tien]} to")
    tong += so_to[tien]

print(f"TONG CONG CO {tong} TO")