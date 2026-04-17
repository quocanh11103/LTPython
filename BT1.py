cd = float(input("Nhap chieu dai day HCN: "))
cr = float(input("Nhap chieu rong day HCN: "))
cc = float(input("Nhap chieu cao khoi HCN: "))
sole = int(input("So thap phan sau phay: "))

DTDay = cd * cr
TheTich = DTDay * cc

print("Diện tích đáy hình chữ nhật = {0:.{1}f} cm\u00b2".format(DTDay, sole))
print("Thể tích hình khối = {0:.{1}f} cm\u00b3".format(TheTich, sole))