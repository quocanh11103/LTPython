from collections import Counter

# Nhập 2 chuỗi
S1 = input("Nhập chuỗi S1: ")
S2 = input("Nhập chuỗi S2: ")

# Chuyển thành Counter
c1 = Counter(S1)
c2 = Counter(S2)

#  Ký tự xuất hiện trong cả 2 chuỗi
common = c1 & c2
print("\nKý tự xuất hiện trong cả 2 chuỗi:")
print(list(common.elements()))

# Đếm ký tự chỉ có ở mỗi chuỗi
only_s1 = set(S1) - set(S2)
only_s2 = set(S2) - set(S1)

print("\nSố ký tự chỉ có trong S1:", len(only_s1))
print("Số ký tự chỉ có trong S2:", len(only_s2))

#In ký tự riêng từng chuỗi
print("\nKý tự có trong S1 nhưng không có trong S2:")
print(list(only_s1))

print("Ký tự có trong S2 nhưng không có trong S1:")
print(list(only_s2))