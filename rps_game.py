import random

def rps_game(guess):
    global wins, loss, draws
    ran_num = random.randint(1,3)
    enemy = ""
    if ran_num == 1:
        enemy = "rock"
    elif ran_num == 2:
        enemy = "paper"
    else:
        enemy = "scissors"

    if guess == enemy:
            draws += 1
            print(f"It is a draw.\nCurrent record is Wins: {wins} Losses: {loss} Draws: {draws}")
           
    elif enemy == "paper":
        if guess == "rock":
            loss += 1
            print(f"You lost!\nCurrent record is Wins: {wins} Losses: {loss} Draws: {draws}")
        else:
            wins += 1
            print(f"You won! wtf\nCurrent record is Wins: {wins} Losses: {loss} Draws: {draws}")
            
    elif enemy == "rock":
        if guess == "scissors":
            loss += 1
            print(f"You lost!\nCurrent record is Wins: {wins} Losses: {loss} Draws: {draws}")
        else:
            wins += 1
            print(f"You won! wtf\nCurrent record is Wins: {wins} Losses: {loss} Draws: {draws}")
    else:
        if guess == "paper":
            loss += 1
            print(f"You lost!\nCurrent record is Wins: {wins} Losses: {loss} Draws: {draws}")
        else:
            wins += 1
            print(f"You won! wtf\nCurrent record is Wins: {wins} Losses: {loss} Draws: {draws}")
    print("The enemy was " + enemy +"\n")


if __name__ == "__main__":
    try:
        wins = 0
        loss = 0
        draws = 0
        while True:
            your_guess = input("What is your fighting stance? ").lower()
            if your_guess not in ("rock", "paper", "scissors"):
                raise ValueError("Please do not enter anything except rock, paper, or scissors.")
            rps_game(your_guess)
        
    except ValueError as e:
        print(f"You entered neither rock nor paper nor scissors.\n{e}")