import math

def la_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def bien_doi_strobogrammatic(n):
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
            return -1

        ket_qua += doi[c]

    return int(ket_qua)


def la_strobogrammatic(n):
    return bien_doi_strobogrammatic(n) == n


for i in range(0, 1000000):

    if la_strobogrammatic(i):
        continue

    if la_nguyen_to(i):
        continue

    strob = bien_doi_strobogrammatic(i)

    if strob != -1 and la_nguyen_to(strob):
        print(i)