from datetime import date

# Nhập ngày thứ nhất
ngay1 = int(input("Nhập ngày thứ nhất: "))
thang1 = int(input("Nhập tháng thứ nhất: "))
nam1 = int(input("Nhập năm thứ nhất: "))

# Nhập ngày thứ hai
ngay2 = int(input("Nhập ngày thứ hai: "))
thang2 = int(input("Nhập tháng thứ hai: "))
nam2 = int(input("Nhập năm thứ hai: "))

d1 = date(nam1, thang1, ngay1)
d2 = date(nam2, thang2, ngay2)

so_ngay_cach_nhau = abs((d2 - d1).days)

print("Số ngày cách nhau giữa 2 ngày là:", so_ngay_cach_nhau)