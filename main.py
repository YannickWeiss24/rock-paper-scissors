import random
import sys

SYMBOLS = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

MAX_PLAYERS = 4
MAX_POINTS = 10

def input_number(text, min= 0, max=1000):
    while True:
        inp = input(str(text))
        if inp == "q":
            sys.exit("Game over")
        if inp.isdigit():
            if int(inp) >= min:
                if int(inp) <= max:
                    return int(inp)
                else:
                    print("Please enter a number below " + str(max) + ".")
            else:
                print("Please enter a number above " + str(min) + ".")
        else:
            print("Please enter a number.")
    

def start_game():
    players = 1
    winning_points = 3
    print("You are Player 1.")
    players = input_number("Against how many other Players do you want to play?", 1, 4)
    winning_points = input_number("How many points do you need to win the game?", 1, 10)
    players += 1
    return (players, winning_points)

def roll_hands(players, round):
    rolls = []
    choice = input_number(f"\nRound {round}\nWhat do you play? Enter 1 for Rock, 2 for Paper, 3 for Scissors.", 1, 3)
    print(f"You play {SYMBOLS[choice]}.")
    rolls.append(choice)
    for i in range(players-1):
        value = random.choice([1,2,3])
        rolls.append(value)
        print(f"Player {i+2} plays {SYMBOLS[value]}.")
    return rolls

def get_points(players, rolls):
    points = []
    for i in range(players):
        if rolls[i] == 3:
            for j in range(players):
                if rolls[j] == 1:
                    points.append(0)
                    break
                if j == players -1: 
                    points.append(1)
                    break
        else:
            for j in range(players):
                if rolls[j] == rolls[i] + 1:
                    points.append(0)
                    break
                if j == players -1: 
                    points.append(1)
                    break
    if max(points) == 0:
        print("Tied. No Player gains points.")
    elif min(points) == 1:
        for i in range(players):
            points[i] += -1
        print("Tied. No Player gains points.")
    else:
        winners = []
        for i in range(players):
            if points[i] == 1:
                winners.append(i+1)
        if points[0] == 1:
            print(f"You won! This rounds winners:", *winners)
        else:
            print(f"You lost! This rounds winners:", *winners)
    return points

def get_winner(points, winning_points):
    winners = []
    for i in range(len(points)):
        if points[i] == winning_points:
            winners.append(i+1)
    return winners

def print_points(round, *points):
    player = 1
    s = f"Points after round {round}: "
    for i in points:
        if player == 1:
            s += f"You: {i}, "
        else:
            s += f"Player {player}: {i}, "
        player += 1
    print(s)

def main():
    while True:
        players, winning_points = start_game()
        current_points = []
        for _ in range(players):
            current_points.append(0)
        round = 0
        while True:
            round += 1
            points = get_points(players, roll_hands(players, round))
            for i in range(players):
                current_points[i] += points[i]
                #print(f"After round {round}, Player {i+1} has {current_points[i]} points.")
            print_points(round, *current_points)
            winners = get_winner(current_points, winning_points)
            if len(winners) > 0:
                if 1 in winners:
                    print(f"\nYou won the game! Winning Players:", *winners)
                else:
                    print(f"\nYou lost the game! Winning Players:", *winners)
                new_game = input_number("New game? Enter 1 for yes, 0 for no.", 0, 1)
                if new_game == 1:
                    break
                else:
                    sys.exit("Bye!")

if __name__ == "__main__":
    main()
