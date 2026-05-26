def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def dem_so_nguyen_to():
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n <= 0:
            print("Vui lòng nhập số nguyên dương!")
            return

        dem = sum(1 for i in range(2, n) if la_so_nguyen_to(i))
        print(f"Số lượng số nguyên tố nhỏ hơn {n}: {dem}")

    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")

dem_so_nguyen_to()