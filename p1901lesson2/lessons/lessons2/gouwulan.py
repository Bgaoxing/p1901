import random

products = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']

count = 200


def get_transaction(n=8):
    pds = []
    p = list(products)
    for i in range(n):
        x = p[random.randint(0, len(p) -1)]
        p.remove(x)
        pds.append(x)
    return pds


with open("./transaction.txt", "w") as fp:
    for i in range(count):
        pds = get_transaction()
        fp.write("T: {}\n".format(",".join(pds)))