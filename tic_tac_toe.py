board=[[" "," "," "],
       [" "," "," "],
       [" "," "," "]]
Dict={1:'00',2:'01',3:'02',4:'10',5:'11',6:'12',7:'20',8:'21',9:'22'}
print(Dict)
for i in range(3):
    for j in range(3):
        player1=int(input("player1-choose a place in the board"))
        if player1==1 and board[0][0]!="0":
            board[0][0]="x"
            print(board)   
        if player1==2 and board[0][1]!="0" :
            board[0][1]="x"
            print(board)   
        if player1==3 and board[0][2]!="0":
            board[0][2]="x"
            print(board)   
        if player1==4 and board[1][0]!="0":
            board[1][0]="x"
            print(board)   
        if player1==5 and board[1][1]!="0":
            board[1][1]="x"
            print(board)   
        if player1==6 and board[1][2]!="0":
            board[1][2]="x"
            print(board)   
        if player1==7 and board[2][0]!="0":
            board[2][0]="x"
            print(board)   
        if player1==8 and board[2][1]!="0":
            board[2][1]="x"
            print(board)
        if player1==9 and board[2][2]!="0":
            board[2][2]="x"
            print(board)   
        player2=int(input("player2-choose a place in the board"))
        if player2==1 and board[0][0]!="x":
            board[0][0]="0"
            print(board)   
        if player2==2 and board[0][1]!="x":
            board[0][1]="0"
            print(board)   
        if player2==3 and board[0][2]!="x":
            board[0][2]="0"
            print(board)   
        if player2==4 and board[1][0]!="x":
            board[1][0]="0"
            print(board)   
        if player2==5 and board[1][1]!="x":
            board[1][1]="0"
            print(board)   
        if player2==6 and board[1][2]!="x":
            board[1][2]="0"
            print(board)   
        if player2==7 and board[2][0]!="x":
            board[2][0]="0"
            print(board)   
        if player2==8 and board[2][1]!="x":
            board[2][1]="0"
            print(board)   
        if player2==9 and board[2][2]!="x":
            board[2][2]="0"
            print(board)   
    if (board[0][0]=="x") and (board[0][1]=="x") and (board[0][2]=="x"):
        print("player1 is a winner !!!!!")
        print(board)
        break
    if (board[1][0]=="x") and(board[1][1]=="x") and (board[1][2]=="x"): 
        print("player1 is a winner !!!!!")
        print(board)
        break
    if board[2][0]=="x" and board[2][1]=="x" and board[2][2]=="x":
        print("player1 is a winner !!!!!")
        print(board)
        break
    if board[0][0]=="0" and board[0][1]=="0" and board[0][2]=="0":
        print("player2 is a winner !!!!!")
        print(board)
        break
    if board[1][0]=="0" and board[1][1]=="0" and board[1][2]=="0":
        print("player2 is a winner !!!!!")
        print(board)
        break
    if board[2][0]=="0" and board[2][1]=="0" and board[2][2]=="0":
        print("player2 is a winner !!!!!")
        print(board)
        break
    if (board[0][0]=="x") and (board[1][0]=="x") and (board[2][0]=="x"):
        print("player1 is a winner !!!!!")
        print(board)
        break
    if (board[0][1]=="x") and(board[1][1]=="x") and (board[2][1]=="x"): 
        print("player1 is a winner !!!!!")
        print(board)
        break
    if board[0][2]=="x" and board[1][2]=="x" and board[2][2]=="x":
        print("player1 is a winner !!!!!")
        print(board)
        break
    if board[0][0]=="0" and board[1][0]=="0" and board[2][0]=="0":
        print("player2 is a winner !!!!!")
        print(board)
        break
    if board[0][1]=="0" and board[1][1]=="0" and board[2][1]=="0":
        print("player2 is a winner !!!!!")
        print(board)
        break
    if board[0][2]=="0" and board[1][2]=="0" and board[2][2]=="0":
        print("player2 is a winner !!!!!")
        print(board)
        break
    if (board[0][0]=="x") and (board[1][1]=="x") and (board[2][2]=="x"):
        print("player1 is a winner !!!!!")
        print(board)
        break
    if (board[0][2]=="x") and(board[1][1]=="x") and (board[2][0]=="x"): 
        print("player1 is a winner !!!!!")
        print(board)
        break
    if board[0][0]=="0" and board[1][1]=="0" and board[2][2]=="0":
        print("player2 is a winner !!!!!")
        print(board)
        break
    if board[0][2]=="0" and board[1][1]=="0" and board[2][0]=="0":
        print("player2 is a winner !!!!!")
        print(board)
        break
print("Game is over!!!!")
