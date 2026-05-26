tri_tuyet_doi = lambda n: n if n >= 0 else -n

n = int(input("Nhập số nguyên n: "))
print(f"Trị tuyệt đối của {n} là: {tri_tuyet_doi(n)}")