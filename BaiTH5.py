n = int(input("Nhập n: "))

tong = 0
tich = 1
while n>0:
    chuso =n%10
    tong+=chuso
    tich*=chuso
    n=n//10
print("Tổng =", tong)
print("Tích =", tich)