score = 0

def game(x,y):
    answer = input(y).lower()
    if answer == x:
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')
    print (score)    

game("central processing unit" , "What is CPU? " )
