s = input("Nhập chuỗi S: ")
word = input("Nhập từ cần đếm: ")

# Đưa về chữ thường
s = s.lower()
word = word.lower()

# Loại bỏ một số dấu câu thường gặp
s = s.replace(",", "")
s = s.replace(".", "")
s = s.replace("!", "")
s = s.replace("?", "")
s = s.replace(";", "")
s = s.replace(":", "")

# Tách chuỗi thành các từ
ds_tu = s.split()

# Đếm số lần xuất hiện của word
dem = 0
for tu in ds_tu:
    if tu == word:
        dem += 1

print("Số từ", word, "là", dem)