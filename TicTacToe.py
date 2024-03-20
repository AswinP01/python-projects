import random
print("**TIC TAC TOE**")
player1=None
player2=None
ht=['head','tail']
rnd=random.choice(ht)
p1c=None
while p1c not in ht:
    p1c=input('Player 1 choose head/tail:')
if p1c=='head':
    print('Player 2: Tail')
    p2c='tale'
else:
    print('Player 2: head')
    p2c='head'
print('Toss:',rnd)
if rnd==p1c:
    print('Player 1 is "X"')
    player1='X'
    player2='O'
else:
    print('player 2 is "X"')
    player2='X'
    player1='O'

w=input("Enter 'Enter' key to continue")
print('This will be our tic tac toe board\n1  | 2 | 3\n---|---|---\n4  | 5 | 6 \n---|---|---\n7  | 8 | 9')

print('*instructions:\n1. Insert the spot number(1-9) to put your sign,\n2. You must fill all 9 spots to get result.')
m=input('''Enter 'Enter' key to continue''')
board_li=[]
for i in range(9):
    board_li.append(' ')

def print_board(board_li):
    board=f'''
     {board_li[0]} | {board_li[1]} | {board_li[2]}
    ---|---|---
     {board_li[3]} | {board_li[4]} | {board_li[5]}
    ---|---|---
     {board_li[6]} | {board_li[7]} | {board_li[8]}
    '''
    print(board)

check_li=[]


def check():
    while True:
        x=int(input('Enter your position:'))
        x-=1    
        if 0<= x < 10:
            if x in check_li:
                print('Spot is blocked')
                continue                      
            check_li.append(x)
            return x
       
        

def ChanceX():
    
    if player1=='X':
        print('Player 1 Chance')
        box=check()        
        board_li[box]='X'
    elif player2=='X':
        print('Player 2 chance')
        box=check()        
        board_li[box]='X'
    print_board(board_li)
    

def ChanceO():

    if player2=='O':
        print('Player 2 chance')
        box=check()        
        board_li[box]='O'
    elif player1=='O':
        print('Player 1 Chance')
        box=check()        
        board_li[box]='O'
    print_board(board_li)

def main():
    print_board(board_li)
    for i in range(1,11):
        if i%2!=0:
            ChanceX()
            if player1=='X':
                if board_li[0]==board_li[1]==board_li[2]=='X' or board_li[3]==board_li[4]==board_li[5]=='X' or board_li[6]==board_li[7]==board_li[8]=='X' or board_li[0]==board_li[3]==board_li[6]=='X' or board_li[1]==board_li[4]==board_li[7]=='X' or board_li[2]==board_li[5]==board_li[8]=='X' or board_li[0]==board_li[4]==board_li[8]=='X' or board_li[2]==board_li[4]==board_li[6]=='X':
                    print(" 'Player 1 Wins' ")
                    print("Congrats,Thankyou for joining the game")
                    break
                elif board_li[0]==board_li[1]==board_li[2]=='O' or board_li[3]==board_li[4]==board_li[5]=='O' or board_li[6]==board_li[7]==board_li[8]=='O' or board_li[0]==board_li[3]==board_li[6]=='O' or board_li[1]==board_li[4]==board_li[7]=='O' or board_li[2]==board_li[5]==board_li[8]=='O' or board_li[0]==board_li[4]==board_li[8]=='O' or board_li[2]==board_li[4]==board_li[6]=='O':
                    print(" 'Player 2 wins' ")
                    print("Congrats,Thankyou for joining the game")
                    break
            else:
                if board_li[0]==board_li[1]==board_li[2]=='X' or board_li[3]==board_li[4]==board_li[5]=='X' or board_li[6]==board_li[7]==board_li[8]=='X' or board_li[0]==board_li[3]==board_li[6]=='X' or board_li[1]==board_li[4]==board_li[7]=='X' or board_li[2]==board_li[5]==board_li[8]=='X' or board_li[0]==board_li[4]==board_li[8]=='X' or board_li[2]==board_li[4]==board_li[6]=='X':
                    print(" 'Player 2 Wins' ")
                    print("Congrats,Thankyou for joining the game")
                    break
                elif board_li[0]==board_li[1]==board_li[2]=='O' or board_li[3]==board_li[4]==board_li[5]=='O' or board_li[6]==board_li[7]==board_li[8]=='O' or board_li[0]==board_li[3]==board_li[6]=='O' or board_li[1]==board_li[4]==board_li[7]=='O' or board_li[2]==board_li[5]==board_li[8]=='O' or board_li[0]==board_li[4]==board_li[8]=='O' or board_li[2]==board_li[4]==board_li[6]=='O':
                    print(" 'Player 1 wins' ")
                    print("Congrats,Thankyou for joining the game")
                    break


        elif i%2==0 and i<10:
            ChanceO()
            if player2=='X':
                if board_li[0]==board_li[1]==board_li[2]=='X' or board_li[3]==board_li[4]==board_li[5]=='X' or board_li[6]==board_li[7]==board_li[8]=='X' or board_li[0]==board_li[3]==board_li[6]=='X' or board_li[1]==board_li[4]==board_li[7]=='X' or board_li[2]==board_li[5]==board_li[8]=='X' or board_li[0]==board_li[4]==board_li[8]=='X' or board_li[2]==board_li[4]==board_li[8]=='X':
                    print(" 'Player 2 Wins' ")
                    print("Congrats,Thankyou for joining the game")
                    break
                elif board_li[0]==board_li[1]==board_li[2]=='O' or board_li[3]==board_li[4]==board_li[5]=='O' or board_li[6]==board_li[7]==board_li[8]=='O' or board_li[0]==board_li[3]==board_li[6]=='O' or board_li[1]==board_li[4]==board_li[7]=='O' or board_li[2]==board_li[5]==board_li[8]=='O' or board_li[0]==board_li[4]==board_li[8]=='O' or board_li[2]==board_li[4]==board_li[8]=='O':
                    print(" 'Player 1 wins' ")
                    print("Congrats,Thankyou for joining the game")
                    break
            else:
                if board_li[0]==board_li[1]==board_li[2]=='X' or board_li[3]==board_li[4]==board_li[5]=='X' or board_li[6]==board_li[7]==board_li[8]=='X' or board_li[0]==board_li[3]==board_li[6]=='X' or board_li[1]==board_li[4]==board_li[7]=='X' or board_li[2]==board_li[5]==board_li[8]=='X' or board_li[0]==board_li[4]==board_li[8]=='X' or board_li[2]==board_li[4]==board_li[8]=='X':
                    print(" 'Player 1 Wins' ")
                    print("Congrats,Thankyou for joining the game")
                    break
                elif board_li[0]==board_li[1]==board_li[2]=='O' or board_li[3]==board_li[4]==board_li[5]=='O' or board_li[6]==board_li[7]==board_li[8]=='O' or board_li[0]==board_li[3]==board_li[6]=='O' or board_li[1]==board_li[4]==board_li[7]=='O' or board_li[2]==board_li[5]==board_li[8]=='O' or board_li[0]==board_li[4]==board_li[8]=='O' or board_li[2]==board_li[4]==board_li[8]=='O':
                    print(" 'Player 2 wins' ")
                    print("Congrats,Thankyou for joining the game")
                    break
        elif i==10:
                print("It's a Draw")
                print("Thankyou for joining the game")
        
      
main()




    


    



