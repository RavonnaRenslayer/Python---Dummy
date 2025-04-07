#Rock, Paper, Scissors Game

def start():
    print ('This is my Rock, Paper, Scissors Game!')
    
    Player_One = input ('Juliana')
    Player_Two = input ('Djair')

    def choices (Player_One_Choice, Player_Two_Choice):

        if Player_One_Choice == 'rock' and Player_Two_Choice == 'paper':
            return ('Paper covers rock! ' + Player_Two + ' wins!')

        elif Player_One_Choice == 'paper' and Player_Two_Choice == 'rock':
            return ('Paper covers rock ' + Player_One + ' wins!')

        elif Player_One_Choice == 'scissors' and Player_Two_Choice == 'paper':
            return ('Scissors cuts paper! ' + Player_One + ' wins!')

        elif Player_One_Choice == 'rock' and Player_Two_Choice == 'scissors':
            return ('Rock smashes scissors! ' + Player_One + ' wins!')

        elif Player_One_Choice == 'paper' and Player_Two_Choice == 'scissors':
            return ('Scissors cuts paper! ' + Player_Two + ' wins!')

        elif Player_One_Choice == 'scissors' and Player_Two_Choice == 'rock':
            return ('Rock smasshes scissors! ' + Player_Two + ' wins!')

        elif Player_One_Choice == Player_Two_Choice:
            return ('Juliana and Djair tied!')

        else:
            return ('Please type Rock, Paper or Scissors!')

Player_One = 'Juliana'
Player_Two = 'Djair'
    
Player_One_Choose = input ('Does ' + Player_One + ' choose Rock, Paper or Scissors? ').lower()

Player_Two_Choose = input ('Does ' + Player_Two + ' choose Rock, Paper or Scissors? ').lower()

print (choices(Player_One_Choose, Player_Two_Choose))

Play_Again()

def Play_Again():
    Again = input ('Would you like to play the game again?').lower()

    if Again == 'No'.lower():
        quit()

    if Again == 'Yes'.lower():
        start()

    else:
        print ('Please enter Yes or No. Thank You!')
        Play_Again()

Play_Again()
start()
