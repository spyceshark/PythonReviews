#imports
import consolemenu
import time
import os
from RunGame import initiate_game

def splash_screen():
    consolemenu.clear_terminal()
    print("\n" * 2)
    print(r" _    _      _                          _  ")
    print(r"| |  | |    | |                        | |")
    print(r"| |  | | ___| | ___ ___  _ __ ___   ___| |")
    print(r"| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ |")
    print(r"\  /\  /  __/ | (_| (_) | | | | | |  __/_|")
    print(r" \/  \/ \___|_|\___\___/|_| |_| |_|\___(_)")
    print("\n" * 1)
    print(r"____________  _____            _____          _____                            ")
    print(r"| ___ \ ___ \/  ___|   ___    /  __ \        |  __ \                           ")
    print(r"| |_/ / |_/ /\ `--.   ( _ )   | /  \/ ___    | |  \/ __ _ _ __ ___   ___  ___  ")
    print(r"|    /|  __/  `--. \  / _ \/\ | |    / _ \   | | __ / _` | '_ ` _ \ / _ \/ __| ")
    print(r"| |\ \| |    /\__/ / | (_>  < | \__/\ (_) |  | |_\ \ (_| | | | | | |  __/\__ \ ")
    print(r"\_| \_\_|    \____/   \___/\/  \____/\___(_)  \____/\__,_|_| |_| |_|\___||___/ ")
    print("\n" * 1)
    print("   _______            _______                 _______")
    print("---'   ____)      ---'   ____)_____       ---'   ____)_____")
    print("      (_____)               _______)                _______)")
    print("      (_____)               ________)            ___________)")
    print("      (____)               ________)            (____)")
    print("---.__(___)       ---.___________)        ---.__(___)")
    print("\n" * 2)
    
    time.sleep(1)

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

    if selection < len(rule_list):
        initiate_game(rule_list[selection])

