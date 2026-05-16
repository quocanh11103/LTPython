import math

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

dem = 0

for n in range(a, b + 1):
    dao = int(str(n)[::-1])   # đảo ngược số

    if math.gcd(n, dao) == 1:
        print(n, end=" ")
        dem += 1

print("\nSố lượng số thân thiện:", dem)