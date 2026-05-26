def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def uoc_so_nguyen_to():
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n <= 0:
            print("Vui lòng nhập số nguyên dương!")
            return

        uoc_nguyen_to = [i for i in range(1, n + 1) if n % i == 0 and la_so_nguyen_to(i)]

        if uoc_nguyen_to:
            print(f"Các số vừa là ước số của {n} là số nguyên tố: {', '.join(map(str, uoc_nguyen_to))}")
        else:
            print(f"{n} không có ước số nào là số nguyên tố.")

    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")

uoc_so_nguyen_to()