#Inports
import time
import consolemenu

#Variables
continue_playing = True
score = [0,0]

#Functions

#clears the terminal screen
def clear_screen():
    print("\n" * 100)


#displays welcome screen
def welcome():
    clear_screen()
    print("Welcome to Rock, Paper, Scissors!")
    print("Its time to play! Lets go!")
    print("\n" * 1)
    print("   _______            _______                 _______")
    print("---'   ____)      ---'   ____)_____       ---'   ____)_____")
    print("      (_____)               _______)                _______)")
    print("      (_____)               ________)            ___________)")
    print("      (____)               ________)            (____)")
    print("---.__(___)       ---.___________)        ---.__(___)")
    time.sleep(6)



#Converts players choice of play into a number for use in algorithm later to determine winner
def play_convert(play_string):
    if play_string == 'R':
        return 0
    elif play_string == 'P':
        return 1
    else:
        return 2


#Displays the score on screen
def show_score():
    score1_string = "Player 1 Total Wins: {}"
    score2_string = "Player 2 Total Wins: {}"
    clear_screen()
    print("Current Score:")
    print(score1_string.format(score[0]))
    print(score2_string.format(score[1]))
    print("\n" * 4)


#prints players hands, showing why a player has won.
def display_hand(input1):
    if input1 =='R':
        print("Rock beats Scissors!")
    elif input1 == 'P':
        print("Paper beats Rock!")
    else:
        print("Scissors beats Paper!")


#determines which player has won this round
def determine_winner(input1, input2):
    global score
    input1_int = play_convert(input1)
    input2_int = play_convert(input2)
    if (input1_int + 1) % 3 == input2_int:
        score[1] += 1
        show_score()
        print("Player 2 Wins!")
        display_hand(input2)
    elif input1_int == input2_int:
        print("Draw!")
    else:
        score[0] += 1
        show_score()
        print("Player 1 Wins!")
        display_hand(input1)


#Gets player input for their choice of play
def input_play():
    valid_bool = False
    while valid_bool == False:
        check_valid = input("Choose your play! (R/P/S): ")
        check_valid = check_valid.upper()
        if check_valid == 'R' or check_valid == 'P' or check_valid == 'S':
            valid_bool = True
        else:
            print("Invalid choice. Choose again.")
    clear_screen()
    return check_valid


#Runs the main game
def play_game():
    show_score()
    print("Player 1! Input your choice! Player 2! Look away now!")
    player1_play = input_play()
    show_score()
    print("Player 2! Input your choice! Player 1! Look away now!")
    player2_play = input_play()
    determine_winner(player1_play, player2_play)


#Check if players wish to continue playing
def continue_function():
    global continue_playing
    valid = False
    while valid == False:
        check = input("Do you want to keep on playing? (Y/N): ")
        check = check.upper()
        if check == 'Y' or check == 'N':
            valid = True
            if check == 'N':
                continue_playing = False
            else:
                continue_playing = True
        else:
            print("Invalid input")


#Welcome Screen
welcome()

#Running Loop
while continue_playing == True:
    play_game()
    continue_function()

clear_screen()



