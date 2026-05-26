import math

hop_le = lambda a, b, c: a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

phan_loai = lambda a, b, c: (
    "Tam giác đều"   if a == b == c else
    "Tam giác vuông cân" if (a == b or b == c or a == c) and
                            sorted([a*a, b*b, c*c])[2] == sorted([a*a, b*b, c*c])[0] + sorted([a*a, b*b, c*c])[1] else
    "Tam giác cân vuông" if (a == b and round(c**2, 9) == round(a**2 + b**2, 9)) or
                            (a == c and round(b**2, 9) == round(a**2 + c**2, 9)) or
                            (b == c and round(a**2, 9) == round(b**2 + c**2, 9)) else
    "Tam giác vuông" if round(sorted([a,b,c])[2]**2, 9) == round(sorted([a,b,c])[0]**2 + sorted([a,b,c])[1]**2, 9) else
    "Tam giác cân"   if a == b or b == c or a == c else
    "Tam giác thường"
)

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if hop_le(a, b, c):
    loai = phan_loai(a, b, c)
    print(f"({a}, {b}, {c}) là 3 cạnh hợp lệ của một tam giác.")
    print(f"Đây là: {loai}.")
else:
    print(f"({a}, {b}, {c}) không tạo thành tam giác hợp lệ.")