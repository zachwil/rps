# Win conditions
TIE = "tie!!\n"
STEVE_WINS = "STONE COLD WINS!!!\n"
ROCK_WINS = "THE ROCK WINS!!!\n"
YOU_WIN = "YOU WIN!!!\n"

PROMPT_USER = "Rock, paper, or scissors baby? "

# Tie game
def tie_game():
    print(TIE)


# You won
def you_win():
    print(YOU_WIN)


# The Rock Won
def the_rock_wins():
    print(ROCK_WINS)
    print(
        """
        ⣶⣿⣾⣷⣷⣾⣿⣿⣿⠋⠀⠀⠀⢠⣾⣿⣿⣿⣶⣤⣤⡀⠀⠀⢀⠀⢹⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣷⣸⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⡿⡟⠀⠀⠀⠀⢿⣿⣿⣿⢷⣿⣿⣿⣿⣿⣿⣿⠿⠁⠃⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⡄⡘⣤⠀⢀⣾⣿⣻⡿⢿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⡉⣩⠀⣦⡙⠟⠟⠛⢓⠀⠙⢿⣿⣿⣿⣿⡧⠀⠀⣾⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⢿⣯⣿⢸⣿⣷⡗⠀⠀⠁⠒⠠⢀⢰⡿⠻⠼⠓⠂⠘⢿⣿⣿⣿
        ⣻⣿⡟⣯⣿⢋⣯⡟⣿⠏⠿⣿⣧⠀⠀⠀⠀⠀⠀⣨⡇⠀⠀⠀⠀⠀⣈⣿⣿⣿
        ⣿⣿⠿⣟⣻⣿⣿⣇⡟⡀⠀⣹⣿⣷⣦⣤⣤⣦⣾⣿⠇⠀⠀⠀⠀⢀⣾⣿⣿⣿
        ⣿⠃⠐⢩⣿⣿⢟⠟⠃⠀⠀⢸⣿⣿⣿⣿⡟⠿⢿⣿⡄⢰⡆⠀⢀⣿⣿⣿⣿⣿
        ⡏⡄⠀⠀⢻⡁⠀⠀⠀⠀⠐⠅⢻⣿⣿⣿⣿⣶⡄⠀⠀⠀⠁⢀⣾⣿⣿⣿⣿⣿
        ⠔⠀⠀⠀⠈⢟⢄⠀⠀⠀⠀⠈⠘⠛⢷⡄⠀⠭⠉⠁⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿
        ⢵⠀⠀⠀⠀⠈⢉⣦⠀⠀⠀⠀⠀⢱⣶⣿⣶⣶⡄⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿
        ⢀⡐⠀⠀⠀⠀⠈⢼⢅⠀⠀⠀⠀⠀⠈⠉⠛⠛⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⠐⠀⠠⡀⠀⠀⠀⠈⠛⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠉⠉⠉⠙⠻⠿⠿⣿⣿
        ⠓⠄⡀⠈⠢⠀⠀⠐⢤⣄⡀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠣⡄⠀⠀⠀⠀⠀⠀⠀
    """
    )


# Steve Austin Won
def steve_austin_wins():
    print(STEVE_WINS)
    print(
        """
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⠟⠋⠉⠛⠛⠫⢍⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⢿⣻⣿⣿⢿⠀⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠹⣟⢿⣿⣿⣿⣿⣿⣿⣿⠏⠁⠈⠉⠉⠉⠉⠉⠉⠘⠛⠀
        ⢨⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡴⠀⢿⣿⣿⣿⣿⣿⡷⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢨⣿⣿⣿⣷⣿⣿⣿⣷⣷⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣢⡸⢤⠀⢻⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⣼⣯⣦⠠⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣷⣯⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠘⠓⣿⢲⡣⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⣿⣿⣿⣿⣿⣿⠛⠀
        ⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⢹⠀⠀⠀⠀⠀⠀⠀⡀⠀⡔⢰⠃⢀⢀⣩⣶⡷⣝⢾⠟⣛⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⡿⣀⠀
        ⢠⣿⣿⣿⣿⣿⣿⣿⡿⠟⠿⣿⣿⣞⣄⠀⠀⠄⢈⣀⣀⣀⠁⣠⣶⣾⣗⡿⢿⣽⡿⠃⢹⣾⡼⢿⢹⣿⣿⣿⣿⠓⣿⣿⣿⣿⣿⡇⡏⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢻⣟⠻⠈⢿⣯⣼⠿⡟⡿⠃⠀⠸⡿⡉⠐⠒⠉⠁⠀⢀⣾⡯⣿⣞⣾⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⡇⡇⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣏⠍⣇⠀⠁⠉⠈⠉⠀⢀⠀⠀⠹⣗⡀⠀⠀⠀⢀⡼⠁⢧⣏⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡇⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣻⣿⡄⠸⠦⡀⠀⠀⠀⡰⣈⣄⠀⣤⣧⡯⠢⠀⠀⢾⡇⠀⢸⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡿⠀
        ⢸⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣼⣿⣿⣄⠇⠁⠊⠀⢠⠃⣸⣩⢻⣟⢿⣿⣴⢤⣄⠈⢇⠀⠈⣇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
        ⢸⣿⣿⣿⡿⠛⠛⠃⠀⠀⠀⣿⣯⠉⣿⣿⣦⠈⢲⢨⣿⣿⣼⠽⡯⠽⠷⠟⢻⣿⣆⡋⢀⡼⠏⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
        ⢨⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⢰⣿⢿⣦⣠⢸⡿⠁⠀⢀⣖⣶⡤⡄⠒⣈⣿⣇⣾⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀
        ⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⢠⢇⡆⣴⣿⠇⠀⢻⣧⡙⢷⣄⡀⠀⠀⠐⠀⣠⣄⢼⣿⣿⡿⠇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
        ⢸⣿⣿⠀⠀⠀⡸⠀⠀⠀⡸⢾⣽⣿⣻⠇⠀⠀⡇⠉⢿⣿⣼⣳⣆⣾⣯⣿⣿⣾⣿⡿⡟⠀⠀⠀⡌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀
        ⢸⣿⡇⠀⠀⠐⠁⠀⠀⠀⠃⠀⠈⠙⡟⠀⠀⢀⣽⢀⠀⠈⠙⣿⠿⡿⣿⣿⣿⡿⠋⠉⠀⠀⠀⣀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⠀
        ⢸⣿⣧⡀⠀⢀⣀⠀⠀⠀⠀⠀⠀⡜⠀⡀⠀⣴⣹⡼⡈⠑⠒⠄⠀⠡⢄⡀⣀⣤⠄⠄⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⠀
        ⢸⣿⣿⣿⣷⣄⣀⣑⡞⠳⠀⢐⣧⢷⠞⡥⢚⣱⣿⠂⢱⣤⣄⣈⣀⣀⣀⣴⣦⣥⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
        ⢰⣿⣿⣿⣿⣿⣿⣍⠋⠓⠢⢐⣟⣐⡂⠠⡋⠈⠁⢠⡎⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⡀⠀⣁⠬⡥⢂⣠⣾⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀
        ⢠⣿⣿⣿⣿⣿⣿⣿⣿⣷⠰⠄⢄⡢⠔⡿⠃⠈⡐⡼⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⢈⠓⠘⣁⣴⠀⣈⡭⢿⠁⢊⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⠁
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠂⠉⠀⠀⠁⢠⣾⠄⠘⣾⣿⣿⣿⣿⣿⣿⣿⣟⣿⠽⠿⠭⠭⠿⢽⣛⣿⣿⣿⣿⣿⣿⡿⠋⠘⣿⣿⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⢠⡟⠁⠀⠀⢻⡯⠿⣿⠻⣿⣿⡿⡇⠀⠀⠀⢸⠀⠀⠀⢀⡈⠙⡟⠻⣿⣟⡅⠀⠀⢹⣿⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠐⠠⠞⠁⠀⠠⠀⢴⡇⠀⠀⡄⠀⠀⠀⠣⡀⠀⠀⠈⠀⠀⡜⢉⡠⠀⡇⠀⠈⠻⢵⡀⠀⣽⣗⠀
        ⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⣺⣷⣶⣶⡆⠀⠰⣤⢴⠁⣶⡢⣠⣄⡜⣰⣿⣷⡄⠳⡄⠀⠀⠀⠀⠀⣿⣿⠀
        ⢰⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠸⣹⣿⡇⠀⠀⢿⣯⣷⡙⢿⡧⠀⢴⡿⣛⣉⠄⣸⡄⠀⠀⢤⣀⠀⣹⡿⠄
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⢰⡯⠀⡏⣿⡇⠀⠀⠘⣻⣻⢠⣀⠠⣿⣆⠦⣀⣤⣀⢹⣣⠀⠀⠘⣵⣯⣿⣷⠀
        ⢰⣿⣿⣿⣿⣿⣿⣿⢏⠀⠀⠀⠀⠀⠀⠀⣰⠁⠀⠀⠈⠇⠀⡗⢹⡇⠀⠀⠀⣿⣷⡧⡉⠟⡀⢤⣺⠩⠛⣩⣽⡿⡀⠀⣰⣿⣿⣿⡿⠀
        ⢸⣿⣿⣿⣿⣿⣿⡟⠀⠄⠀⠀⠀⠀⠀⠀⢽⠀⠀⠀⠀⢩⢠⡗⠸⣷⡀⣠⣶⣿⣿⣿⣿⡄⠿⣿⡟⠀⠰⣷⣿⣿⣧⣾⣿⣿⣿⣿⣿⠀
        ⢸⣿⣿⣿⣿⣿⣿⡇⠀⠆⠀⠀⠀⠀⠀⠼⠏⠀⠀⠄⠀⣷⠋⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣳⣀⠀⠀⢀⣠⣷⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀
        ⢸⣿⣿⣿⣿⣿⣿⠻⠀⡀⠀⠀⠀⠀⠀⠐⢛⠀⢀⡃⠈⢯⠐⠠⣄⡿⠛⠉⢹⣿⣿⣿⣿⡷⣾⣭⣿⣿⣿⣿⡿⠋⣾⣿⣿⣿⣿⣿⡵⠀
        ⢸⣿⣿⣿⣿⣿⡏⢀⡇⡘⢦⡀⠀⠀⠀⢠⡆⢀⣚⡼⠃⢹⠠⢸⣋⡄⠀⠀⠸⣽⣿⣟⠁⠀⠹⣿⣿⣿⣿⣏⡀⠀⣿⣿⣿⣿⣿⣿⡳⠀
        ⢸⣿⣿⣿⣿⣿⣧⡘⣞⡪⠢⣁⠀⠀⢠⡿⠀⠀⠈⡤⢠⠟⡀⢸⢿⣧⡆⢀⣴⣿⣿⡏⠀⠀⡀⠈⢻⣿⣇⡆⠀⠀⡿⣿⣿⣿⣿⣿⡇⠀
        ⢘⣿⣿⣿⣿⣿⣿⣷⡿⣙⡽⢖⠀⠤⠬⠅⡄⠀⠋⠠⣢⡞⣩⣟⣿⣿⣿⣿⣿⣿⣿⠀⠀⢢⣷⡀⠀⢻⣿⢃⠀⠀⢹⣿⣿⣿⣿⣿⣿⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣄⠱⡀⠁⠢⣀⡀⠀⠠⠴⠛⡹⢮⣱⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣷⠀⠈⣿⣿⠀⠀⢸⣿⡿⠟⠻⣿⣯⠄
        ⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣏⡀⣀⠄⣈⡀⡀⣄⢀⠀⢁⣿⣟⣻⣻⣛⣿⣻⣿⣿⣲⡶⣮⡿⡟⠖⢶⣾⣟⡷⢲⠶⠳⠴⢶⠆⣿⡿⠁
    """
    )


def ask_to_play_winner(winner):
    print(f"Want to square off with {str(winner)}?")
    user_choice = input(PROMPT_USER)
    print()  # adding additional space
    return user_choice


def show_player_results(
    player_1_choice, player_1_name, player_2_choice, player_2_name="You"
):
    print(f"{player_1_name} picked: {str(player_1_choice)}!")
    print(f"{player_2_name} picked: {str(player_2_choice)}!")