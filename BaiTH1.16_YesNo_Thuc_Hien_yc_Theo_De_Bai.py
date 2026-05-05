def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập dữ liệu
numbers = []

while True:
    n = int(input("Nhập số nguyên: "))
    numbers.append(n)
    
    tiep = input("Tiếp tục? (Y/N): ").upper()
    if tiep == 'N':
        break

# a) In số nguyên tố
print("\nCác số nguyên tố trong list:")
for x in numbers:
    if is_prime(x):
        print(x, end=" ")

# b) Trung bình số âm và dương
sum_am = count_am = 0
sum_duong = count_duong = 0

for x in numbers:
    if x < 0:
        sum_am += x
        count_am += 1
    elif x > 0:
        sum_duong += x
        count_duong += 1

if count_am > 0:
    print("\nTrung bình số âm:", sum_am / count_am)
else:
    print("\nKhông có số âm")

if count_duong > 0:
    print("Trung bình số dương:", sum_duong / count_duong)
else:
    print("Không có số dương")

# c) Max, Min
print("Số lớn nhất:", max(numbers))
print("Số nhỏ nhất:", min(numbers))

# d) Kiểm tra tăng dần
is_increasing = True
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_increasing = False
        break

if is_increasing:
    print("Danh sách đã tăng dần")
else:
    print("Danh sách chưa tăng dần")