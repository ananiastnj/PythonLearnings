def start_game():
    for i in range(1,8):
        rs["r_kuli{}".format(i)] = 5
        ls["l_kuli{}".format(i)] = 5

def rstart():
    kuli_en = int(input("Enter a number 1-7: "))
    muthu = rs["r_kuli{}".format(kuli_en)]
    rs["r_kuli{}".format(kuli_en)] = 0
    print(muthu)
    rcount(muthu,kuli_en)

def lcount(muthu,kuli_en):
    for i in range(muthu):
        kuli_en += 1
        ls["l_kuli{}".format(kuli_en)] = ls["l_kuli{}".format(kuli_en)] + 1
        muthu -= 1
        if (kuli_en > 6):
            kuli_en = 0
            rcount(muthu,kuli_en)
            break

def rcount(muthu,kuli_en):
    for i in range(muthu):
        kuli_en += 1
        rs["r_kuli{}".format(kuli_en)] = rs["r_kuli{}".format(kuli_en)] + 1
        muthu -= 1
        if(kuli_en > 6):
            kuli_en = 0
            lcount(muthu,kuli_en)
            break
muthu = 0
kuli_en = 0
rp = 0
lp = 0
rs = {}
ls = {}
start_game()
print(rs)
print(ls)
#print(rs["r{}".format(1)])
rstart()
print(rs)
print(ls)