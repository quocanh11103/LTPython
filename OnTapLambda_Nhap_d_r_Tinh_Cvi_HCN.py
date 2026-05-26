chu_vi_hcn = lambda d, r: 2 * (d + r)

d = float(input("Nhập chiều dài d: "))
r = float(input("Nhập chiều rộng r: "))
print(f"Chu vi hình chữ nhật ({d} x {r}) = {chu_vi_hcn(d, r):.4f}")