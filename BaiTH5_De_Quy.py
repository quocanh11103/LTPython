def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Nhập số nguyên dương n: "))

if n < 0:
    print("n phải là số nguyên dương")
else:
    print("Số hạng Fibonacci thứ", n, "là:", fibonacci(n))