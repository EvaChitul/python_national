'''Make a two-player Rock-Paper-Scissors game.
    Rock beats scissors
    Scissors beats paper
    Paper beats rock'''


def main_menu():
    while True:
        action = input ('Welcome to Rock Paper Scissors! Please choose an option. Type: \n'
                        'N for a new game \n'
                        'Q to quit \n')

        if action.lower() == 'n':
            new_game()
        else:
            print('Thanks for playing! See you soon \n')
            break

def new_game():
    print('Starting New Game!')
    player_1 = (input('Player 1: Insert Your Option: Rock/Paper/Scissors: ')).lower()
    player_2 = (input('Player 2: Insert Your Option: Rock/Paper/Scissors: ')).lower()

    if player_1 == player_2:
        print ('It\'s a tie! Play again \n')
        new_game()
    elif player_1 == 'rock' and player_2 == 'paper':
        print('Paper beats rock! Player 2 wins!\n')
    elif player_1 == 'paper' and player_2 == 'rock':
        print('Paper beats rock! Player 1 wins!\n')
    elif player_1 == 'rock' and player_2 == 'scissors':
        print('Rock beats scissors! Player 1 wins!\n')
    elif player_1 == 'scissors' and player_2 == 'rock':
        print('Rock beats scissors! Player 2 wins!\n')
    elif player_1 == 'scissors' and player_2 == 'paper':
        print('Scissors beats paper! Player 1 wins!\n')
    else:
        print('Scissors beats paper! Player 2 wins!\n')
    main_menu()


main_menu()


