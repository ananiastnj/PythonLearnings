class pallanguli:
    total_muthu = 70
    player1 = 35
    player2 = 35
    board = []
    # print(board)
    player1_side_board = 0
    player2_side_board = 0
    player1_start = 0
    player2_start = 0
    player1_kuli = 0
    player2_kuli = 0
    total_kuli = 0
    def index_check(self,start_value, total_kuli):
        if (start_value == 13):
            start_value = -1
        return start_value

    def round_calculation(self,player1_side_board,player2_side_board,player1_start,player2_start,player1,player2,board):
        print("ROUND OVER")
        if(player1_side_board == 0):
            for i in range(7,14):
                player2 += board[i]
                board[i] = 0
        elif(player2_side_board == 0):
            for i in range(7):
                player1 += board[i]
                board[i] = 0
        print("***** BOARD *****\n",board)
        print("player1",player1)
        print("player2",player2)
        if(player1 > player2):
            print("Player1 Lead the game")
        elif(player1 < player2):
            print("Player1 Lead the game")
        elif(player1 == player2):
            print("Both are equal")

    def game_start(self, player1_side_board, player2_side_board, player1_start, player2_start, player1, player2,board):
        while(player2_side_board > 0 and player1_side_board > 0):
            print("Player1 starting the game ")
            player1_start = int(input("Player1 -> Please enter a number 0-6 : "))
            while(player1_start < 0 or player1_start  > 6):
                player1_start = int(input("Player1 -> Please enter a number 0-6 : "))
            moving_muthu = board[player1_start]
            board[player1_start] = 0
            while(moving_muthu != 0):
                player1_start = index_check(player1_start)
                player1_start += 1
                board[player1_start] +=1
                moving_muthu -= 1
                player1_start = index_check(player1_start)
                if(moving_muthu == 0):
                    player1_start += 1
                    if(board[player1_start] == 0):
                        player1_start = index_check(player1_start)
                        player1 += board[player1_start+1]
                        board[player1_start + 1] = 0
                        break
                    else:
                        moving_muthu = board[player1_start]
                        board[player1_start] = 0
            print("PLAYER 1 Completed - Calculated counts")
            print(board)
            sum = 0
            for i in range(7):
                sum += board[i]
            player1_side_board = sum
            sum = 0
            for i in range(7,14):
                sum += board[i]
            player2_side_board = sum
            sum = 0
            print("Player1 Board : ",player1_side_board)
            print("Player2 Board : ",player2_side_board)
            print("player1",player1)
            print("player2",player2)
            print("Player2 starting the game ")
            player2_start = int(input("player2 -> Please enter a number 7-13 : "))
            while (player2_start < 7 and player2_start > 13):
                player2_start = int(input("Player2 -> Please enter a number 7-13 : "))
            moving_muthu = board[player2_start]
            board[player2_start] = 0
            while(moving_muthu != 0):
                player2_start = index_check(player2_start)
                player2_start += 1
                board[player2_start] +=1
                moving_muthu -= 1
                player2_start = index_check(player2_start)
                if(moving_muthu == 0):
                    player2_start += 1
                    if(board[player2_start] == 0):
                        player2_start = index_check(player2_start)
                        player2 += board[player2_start+1]
                        board[player2_start + 1] = 0
                        break
                    else:
                        moving_muthu = board[player2_start]
                        board[player2_start] = 0
            print("PLAYER 2 Completed - Calculated counts")
            print(board)
            sum = 0
            for i in range(7):
                sum += board[i]
            player1_side_board = sum
            sum = 0
            for i in range(7,14):
                sum += board[i]
            player2_side_board = sum
            sum = 0
            print("Player1 Board : ",player1_side_board)
            print("Player2 Board : ",player2_side_board)
            print("player1",player1)
            print("player2",player2)

    def board_generation(self, player1, player2, board):
        player1_kuli = player1 // 5
        #board = []
        if(player1_kuli < 7 ):
            board = [5 for i in range(player1_kuli)]
            player1 -= (player1_kuli*5)
        elif(player1_kuli >= 7):
            board = [5 for i in range(7)]
            player1 -= (7 * 5)
        player2_kuli = player2 // 5
        if (player2_kuli < 7):
            board.extend([5 for i in range(player2_kuli)])
            player2 -= (player2_kuli * 5)
        elif (player2_kuli >= 7):
            board.extend([5 for i in range(7)])
            player2 -= (7 * 5)
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.total_kuli = len(board)
'''    print(board)
    print(player1)
    print(player2)
'''
#Creating board

p = pallanguli()
p.board_generation(player1, player2, board)
print(board)
print(player1)
print(player2)
print(player1_kuli)
print(player2_kuli)
print(total_kuli)
#game_start(player1_side_board,player2_side_board,player1_start,player2_start,player1,player2,board)
#round_calculation(player1_side_board,player2_side_board,player1_start,player2_start,player1,player2,board)
