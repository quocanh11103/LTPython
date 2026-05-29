import math
#hàm in ra bảng cưu chương từ a-b (a<b) hoặc từ b-a(b<a)
def bang_cuu_chuong(a, b):
    if a < b:
        for i in range(a, b + 1):
            print(f"\nBảng cửu chương {i}")
            for j in range(1, 11):
                print(f"{i} x {j} = {i*j}")
    else:
        for i in range(b, a + 1):
            print(f"\nBảng cửu chương {i}")
            for j in range(1, 11):
                print(f"{i} x {j} = {i*j}")
#Hàm xử lý kiểm tra có phải số nguyên tố không
def la_so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
#In ra số nguyên tố
def liet_ke_so_nguyen_to(n):
    print("Các số nguyên tố nhỏ hơn", n, "là:")
    for i in range(2, n):
        if la_so_nguyen_to(i):
            print(i, end=" ")

#Hàm in và kiểm tra vừa là ước số vừa là số nguyên tố
def uoc_so_nguyen_to(n):
    print("\nCác ước số nguyên tố của", n, "là:")
    for i in range(1, n + 1):
        if n % i == 0 and la_so_nguyen_to(i):
            print(i, end=" ")

# hàm input thông tin
a, b = map(int, input("Nhập số a, b cách nhau bằng dấu phẩy: ").split(","))
# gọi hàm in bảng cửu chương
bang_cuu_chuong(a, b)
#Nhập và gọi hàm in ra các số nguyên tố
n = int(input("\nNhập n để liệt kê số nguyên tố: "))
liet_ke_so_nguyen_to(n)
#nhập và gọi hàm in và kiểm tra vừa là ước số vừa là số nguyên tố 
m = int(input("\nNhập số cần tìm ước số nguyên tố: "))
uoc_so_nguyen_to(m)