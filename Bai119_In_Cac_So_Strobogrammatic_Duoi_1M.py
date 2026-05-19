def la_strobogrammatic(n):
    s = str(n)

    doi = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    ket_qua = ""

    for c in reversed(s):
        if c not in doi:
            return False
        ket_qua += doi[c]

    return ket_qua == s


for i in range(0, 1000000):
    if la_strobogrammatic(i):
        print(i)