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
def p1side_list(p1,p1Total):
    if(p1Total >= 35):
        p1side = [5,5,5,5,5,5,5]
        p1Total -= 35
    elif(p1Total < 35):
        p1kuli = p1Total//5
        for i in range(p1kuli):
            p1side[i] = 5
            p1Total -= 5

total_muthu = 70
p1Total = total_muthu/2
p2Total = total_muthu/2


