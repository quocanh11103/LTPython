#Hàm lambda Nhập và kiểm tra có là bội số của 13 và 19 không
kiem_tra = lambda n: n % 13 == 0 or n % 19 == 0

n = int(input("Nhập số nguyên n: "))

if kiem_tra(n):
    print(n, "là bội của 13 hoặc 19")
else:
    print(n, "không là bội của 13 hoặc 19")

#Hàm lambda kiểm tra tam giác
tam_giac = lambda a, b, c: (
    "Không phải tam giác"
    if a + b <= c or a + c <= b or b + c <= a
    else "Tam giác đều"
    if a == b == c
    else "Tam giác cân"
    if a == b or a == c or b == c
    else "Tam giác vuông"
    if a*a + b*b == c*c
    or a*a + c*c == b*b
    or b*b + c*c == a*a
    else "Tam giác thường"
)
# Hàm nhập thông tin tam giác
a = int(input("\nNhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
#hàm xuất thông tin kiểm tra tam giác
print("Kết quả:", tam_giac(a, b, c))