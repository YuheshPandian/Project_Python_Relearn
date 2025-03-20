from random import choice

player_choice : str = input("Choose Rock/Paper/Scissors [r/p/s]: ").lower()

choices : list = ['r','p','s']
actual_options : dict = {'r':"Rock 🪨",'p':"Paper 📜",'s':"Scissors ✂️"}

bot_choice : str = choice(choices)

def player_won():
    # printing the choices made by players
    print(f"👨 You chose: {actual_options[player_choice]}")
    print(f"🤖 Bot chose: {actual_options[bot_choice]}")

    print("Hurray! You won 🎉")

def bot_won():
    # printing the choices made by players
    print(f"👨 You chose: {actual_options[player_choice]}")
    print(f"🤖 Bot chose: {actual_options[bot_choice]}")

    print("Opps! the bot won 😢")


if player_choice == bot_choice:
    print(f"Both of you chose {actual_options[player_choice]}")
    print("It is a draw 🤝.")
elif player_choice == "s":
    if bot_choice == "r":
        bot_won()
    else:
        player_won()
elif player_choice == "r":
    if bot_choice == "p":
        bot_won()
    else:
        player_won()
elif player_choice == "p":
    if bot_choice == "s":
        bot_won()
    else:
        player_won()
else:
    print('Please give a valid input :<')