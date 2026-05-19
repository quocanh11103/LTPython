import math

def la_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


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
    if la_strobogrammatic(i) and la_nguyen_to(i):
        print(i)