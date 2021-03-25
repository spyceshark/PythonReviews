#Inports
import time
import consolemenu
import os
import json


#Variables
continue_playing = True
score = [0,0]


#Displays the score on screen
def show_score():
    score_string = "Current Scores:   Player 1 [{0}|{1}] Player 2"
    return score_string.format(score[0], score[1])


#
def compare_matchup(rules_dictionary, player, opponent):
    win_or_lose = False
    winning_matchups = rules_dictionary.get(player)
    if isinstance(winning_matchups, str) == True:
        if winning_matchups == opponent:
            win_or_lose = True
    else:
        for i in winning_matchups:
            if i == opponent:
                win_or_lose = True

    return win_or_lose


#determines which player has won this round
def determine_winner(rules_dictionary, player_one_play, player_two_play):
    global score
    player_one_win = False
    player_two_win = False
    result = 0      #0 = Tie |  1 = player 1 win |  2 = player 2 win
    if player_one_play == player_two_play:
        return result

    player_one_win = compare_matchup(rules_dictionary, player_one_play, player_two_play)
    player_two_win = compare_matchup(rules_dictionary, player_two_play, player_one_play)

    if player_one_win == player_two_win:
        return result
    elif player_one_win == True:
        result = 1
        score[0] += 1
    elif player_two_win == True:
        result = 2
        score[1] += 1
    
    return result


#Gets player input for their choice of play
def input_play(player_number, rules_dictionary):
    menu_string = "Player {0}! Please input your choice! Player {1}! Please Look away!"
    menu_string = menu_string.format(player_number + 1, ((player_number + 1) % 2) + 1)
    play_options = list(rules_dictionary.keys())
    menu = consolemenu.SelectionMenu(play_options, show_score(), menu_string)
    menu.show_exit_option = False
    menu.show()
    menu.join()
    return play_options[menu.selected_option]


#
def display_results(results, player_one_play, player_two_play):
    global continue_playing
    results_menu_string = ""
    results_menu_play = ""
    list_selection = ["Yes", "No"]

    if results == 0 :
        results_menu_string = "TIE!"
        results_menu_play = "{0} Ties with {1}"
        results_menu_play = results_menu_play.format(player_one_play, player_two_play)
    elif results == 1 :
        results_menu_string = "Player 1 Wins!"
        results_menu_play = "{0} Beats {1}"
        results_menu_play = results_menu_play.format(player_one_play, player_two_play)
    elif results == 2 :
        results_menu_string = "Player 2 Wins!"
        results_menu_play = "{0} Beats {1}"
        results_menu_play = results_menu_play.format(player_two_play, player_one_play)

    results_menu = consolemenu.SelectionMenu(list_selection, show_score(), results_menu_string + " " + results_menu_play)
    results_menu.prologue_text = "Do you want to play again?"
    results_menu.show_exit_option = False
    results_menu.show()
    results_menu.join()
    if results_menu.selected_option == 1:
        continue_playing = False


#Runs the main game
def play_game(rules_dictionary):
    while continue_playing == True:
        consolemenu.clear_terminal()
        current_player = 0
        player_one_play = input_play(current_player, rules_dictionary)
        current_player += 1
        player_two_play = input_play(current_player, rules_dictionary)

        result = determine_winner(rules_dictionary, player_one_play, player_two_play)
        display_results(result, player_one_play, player_two_play)
    

#Initiates the game with the file and game choice of the player
def initiate_game(rules_file):
    cur_dir = os.getcwd()
    with open(cur_dir + "\\RockPaperScissors\\Rules\\" + rules_file) as json_file:
        rules_dictionary = json.load(json_file)
    play_game(rules_dictionary)