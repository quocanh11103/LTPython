def in_bang_cuu_chuong(n):
    print(f"\n Bảng cửu chương {n} ")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def nhap_va_in_bang_cuu_chuong():
    try:
        dong = input("Nhập 2 số nguyên a, b (cách nhau bởi dấu phẩy): ")
        a, b = map(int, dong.split(','))

        if a < b:
            for n in range(a, b + 1):
                in_bang_cuu_chuong(n)
        elif b < a:
            for n in range(a, b - 1, -1): 
                in_bang_cuu_chuong(n)
        else:
            in_bang_cuu_chuong(a)

    except ValueError:
        print("Vui lòng nhập đúng định dạng: 2 số nguyên cách nhau bởi dấu phẩy!")

nhap_va_in_bang_cuu_chuong()