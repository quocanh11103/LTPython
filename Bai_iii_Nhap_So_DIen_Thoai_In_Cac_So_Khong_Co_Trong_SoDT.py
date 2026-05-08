

S = input("Nhập số điện thoại: ")

tap_so = set(S)   # chuyển các ký tự trong S thành tập hợp

print("Các số không xuất hiện là:")

for i in range(10):
    if str(i) not in tap_so:
        print(i, end=" ")