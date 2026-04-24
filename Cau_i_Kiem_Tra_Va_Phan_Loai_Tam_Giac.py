# Hàm lambda kiểm tra 3 cạnh tam giác và phân loại
phan_loai_tam_giac = lambda a, b, c: (
    "Không phải tam giác" if not (a + b > c and a + c > b and b + c > a)
    else "Tam giác đều" if a == b == c
    else "Tam giác vuông cân" if (a == b or b == c or c == a) and (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2)
    else "Tam giác vuông" if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2)
    else "Tam giác cân" if a == b or b == c or c == a
    else "Tam giác thường"
)

a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
print(f"Kết quả: {phan_loai_tam_giac(a, b, c)}")