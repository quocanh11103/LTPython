def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def liet_ke_so_nguyen_to():
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n <= 0:
            print("Vui lòng nhập số nguyên dương!")
            return

        danh_sach = [i for i in range(2, n) if la_so_nguyen_to(i)]

        if danh_sach:
            print(f"Các số nguyên tố nhỏ hơn {n}: {', '.join(map(str, danh_sach))}")
        else:
            print(f"Không có số nguyên tố nào nhỏ hơn {n}.")

    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")

liet_ke_so_nguyen_to()