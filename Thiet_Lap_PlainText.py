cipher = input("Nhập chuỗi nén: ")

plain = ""
i = 0

while i < len(cipher):
    if cipher[i] == '#':
        so_lan = int(cipher[i + 1])   # số lần lặp
        ky_tu = cipher[i + 2]         # ký tự cần lặp
        
        plain += ky_tu * so_lan
        i += 3
    else:
        plain += cipher[i]
        i += 1

print("Chuỗi gốc là:", plain)