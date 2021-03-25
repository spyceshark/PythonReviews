#imports
import consolemenu
import time
import os
from RunGame import initiate_game

def splash_screen():
    consolemenu.clear_terminal()
    print("\n" * 2)
    print(" _    _      _                          _  ")
    print("| |  | |    | |                        | |")
    print("| |  | | ___| | ___ ___  _ __ ___   ___| |")
    print("| |/\\| |/ _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ |")
    print("\\  /\\  /  __/ | (_| (_) | | | | | |  __/_|")
    print(" \\/  \\/ \\___|_|\\___\\___/|_| |_| |_|\\___(_)")
    print("\n" * 1)
    print("Welcome to Rock, Paper, Scissors!")
    print("Its time to play! Lets go!")
    print("\n" * 1)
    print("   _______            _______                 _______")
    print("---'   ____)      ---'   ____)_____       ---'   ____)_____")
    print("      (_____)               _______)                _______)")
    print("      (_____)               ________)            ___________)")
    print("      (____)               ________)            (____)")
    print("---.__(___)       ---.___________)        ---.__(___)")
    print("\n" * 2)
    
    time.sleep(5)

def read_rules():
    path = os.getcwd() + "\\RockPaperScissors\\Rules"
    rule_files = []

    with os.scandir(path) as listOfEntries:
        for entry in listOfEntries:
            # print all entries that are files
            if entry.is_file():
                rule_files.append(entry.name)
                print(entry.name)
    return rule_files

def main_menu_start():  
    splash_screen()
    #menu = consolemenu.ConsoleMenu("Rock Paper Scissors", "Choose your game mode",)
    rule_list = read_rules()
    menu = consolemenu.SelectionMenu(rule_list, "RPS & Co. Games", "Please choose your game mode!")
    menu.show()
    menu.join()
    selection = menu.selected_option

    #if bool(selection) == True:
    initiate_game(rule_list[selection])

