import random


def writec(ind):
    f = open(ind, "w")
    l = [[i for i in range(32, 128)], [random.randint(1000000, 9999999) for i in range(32, 128)]]
    lrus = [[i for i in range(1040, 1104)], [random.randint(1000000, 9999999) for i in range(1040, 1104)]]
    l[0] += lrus[0]
    l[1] += lrus[1]
    random.shuffle(l[0])
    random.shuffle(l[1])
    for i in l[0]:
        f.write(str(i) + " ")
    f.write("\n")
    for i in l[1]:
        f.write(str(i) + " ")
    f.close()