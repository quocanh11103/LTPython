from datetime import datetime, timedelta

now = datetime.now()
sau_5_giay = now + timedelta(seconds=5)

print("Thời gian hiện tại:", now.strftime("%d/%m/%Y %H:%M:%S"))
print("Thời gian sau khi thêm 5 giây:", sau_5_giay.strftime("%d/%m/%Y %H:%M:%S"))