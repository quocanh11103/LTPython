# Nhập thông tin xủ lý
dai = float (input("Nhập chiều dài đáy hình khối chữ nhật: "));
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật: "));
cao = float(input("Nhập chiều cao đáy hình hộp chữ nhật: "));
n=int(input("Số lượng số lẻ cần hiển thị : "));

# Xử lý thông tin
dientichday=dai * rong;
thetichkhoi=dai * rong* cao;

#Xuất thông tin ra màn hình
print("Diện tích đáy hình chữ nhật = ",round(dientichday,n),"cm\u00b2");
print("Thể tích hình khối = ",round(thetichkhoi,n),"cm\u00b3");


      