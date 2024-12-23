import msvcrt
import random


def main():
    
    print("Welcome to Rock, Paper, Scissors!\nThis game was developed by Paul")

    while True:
        option = input("\nStart game (y/n): ")
        
        if option == "y":
            mode_chosen = game_modes()
            player1, player2 = player_names(mode_chosen)
            play_game(mode_chosen, player1, player2)
        else:
            print("Goodbye!")
            exit()
  
  
def game_modes():
    print("""\nGame modes:
        1 - Human vs Human
        2 - Human vs Computer""")
    mode_chosen = input("\nChoose game mode (1 or 2 or exit): ")
    if mode_chosen == '1':
        print("Human vs Human")
    elif mode_chosen == '2':
        print("Human vs Computer")
    elif mode_chosen == "exit":
        print("Goodbye!")
        exit()
    else:
        print("""Please enter a valid option.
            Type exit to quit the game""")
    return mode_chosen


def player_names(mode_chosen):
    if mode_chosen == '1':
        player1 = input("Enter Player1 name: ")
        player2 = input("Enter Player2 name: ")
    elif mode_chosen == '2':
        player1 = input("Enter Player1 name: ")
        player2 = "Computer"
    print(f"\nPlayer1: {player1} vs Player2: {player2}")
    return player1, player2


def play_game(mode_chosen, player1, player2):

    print("""\nGame rules: 
          Rock beats Scissors
          Scissors beats Paper
          Paper beats Rock""")
    
    choices_message = """\nInstructions: Press 
            1 for Rock, 
            2 for Paper, 
            3 for Scissors\n"""
        
    while True:
        
        if mode_chosen == '1':
            print(choices_message)
            player1_choice = int(choice(player1))
            player2_choice = int(choice(player2))
            object_played(player1, player1_choice)
            object_played(player2, player2_choice)
            print(winner(player1, player2, player1_choice, player2_choice))
            break
        
        elif mode_chosen == '2':
            print(choices_message)
            player1_choice = int(choice(player1))
            player2_choice = int(random_choice())
            object_played(player1, player1_choice)
            object_played(player2, player2_choice)
            print(winner(player1, player2, player1_choice, player2_choice))
            break
       

def masked_input(prompt=""):
    print(prompt, end="", flush=True)
    actual_input = ""
    while True:
        char = msvcrt.getch()  # Get a single character
        if char == b'\r':  # Enter key (Carriage Return)
            print()  # Move to the next line
            break
        elif char == b'\x08':  # Backspace key
            if actual_input:  # Only if there are characters to delete
                actual_input = actual_input[:-1]
                print("\b \b", end="", flush=True)
        else:
            actual_input += char.decode('utf-8')  # Decode byte to string
            print("*", end="", flush=True)
    return actual_input


def choice(player):
    while True:
        p_choice = masked_input(f"{player} enter your choice: ")
        if p_choice in ['1', '2', '3']:
            return int(p_choice)
        elif p_choice == "exit":
            print("Goodbye!")
            exit()           
        else:
            print("""Please enter a valid option.
                Type exit to quit the game""")

       
def object_played(player, p_choice):
    if p_choice == 1:
        object_played = f"{player} chose Rock"
    elif p_choice == 2:
        object_played = f"{player} chose Paper"
    elif p_choice == 3:
        object_played = f"{player} chose Scissors"
    else:
        print("\nInvalid choice")
    print(object_played)

    
def winner(player1, player2, player1_choice, player2_choice):  
    if player1_choice == 1 and player2_choice == 3:
        result = f"{player1} wins!"
    elif player1_choice == 2 and player2_choice == 1:
        result = f"{player1} wins!"
    elif player1_choice == 3 and player2_choice == 2:
        result = f"{player1} wins!"
    elif player1_choice == 1 and player2_choice == 2:
        result = f"{player2} wins!"
    elif player1_choice == 2 and player2_choice == 3:
        result = f"{player2} wins!"
    elif player1_choice == 3 and player2_choice == 2:
        result = f"{player2} wins!"
    else:
        result = "It's a tie!"
    return result
    
def random_choice():
    return random.randint(1, 3)

    
if __name__ == "__main__":
    main()
    





