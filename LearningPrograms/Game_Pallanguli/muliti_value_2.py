'''
Pallanguli game
Rules :
1. Total 70 muthu
2. P1 = 35 muthu
3. P2 = 35 muthu
4. p1 start the game from right side - he has 7 kuzhi
5. p2 also has the 7 kuzhi. Each kuzhi get 5 muthu in the beginging
6.


'''

def p1_start():
    kuli_en = int(input("Enter 0 - 6 : "))
    muthu = p1side[kuli_en]
    p1side[kuli_en] = 0
    kuli_en += 1
    p1sideCount(muthu,kuli_en)

def p1sideCount(muthu,kuli_en):
    for i in range(muthu):
        p1side[kuli_en] += 1
        muthu -= 1
        kuli_en += 1
        if(kuli_en == 7): #6 < 7
            kuli_en = 0
            p2sidecount(muthu,kuli_en)
            break

def p2sidecount(muthu,kuli_en):
    for i in range(muthu):
        p2side[kuli_en] += 1
        muthu -= 1
        kuli_en += 1
        if(muthu == 0):
            if(p2side[kuli_en] == 0):
                p1 = p1 + p2side[kuli_en+1]
                break
            else:
                muthu = p2side[kuli_en]
                break
        if(kuli_en == 7): #6 < 7
            kuli_en = 0
            p2sidecount(muthu,kuli_en)
            break

p1,p2,kuli_en,muthu = 0,0,0,0
p1side = [5,5,5,5,5,5,5]
p2side = [5,5,5,5,5,5,5]
print(p1side)
print(p2side)
p1_start()
print(p1side)
print(p2side)