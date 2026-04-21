from datetime import datetime

s = input("Nhập chuỗi ngày theo dạng 'Sep 18 2019 2:43PM': ")

dt = datetime.strptime(s, "%b %d %Y %I:%M%p")

print("Chuỗi sau khi chuyển sang kiểu ngày giờ là:", dt)
print("Kiểu dữ liệu:", type(dt))