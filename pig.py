import random

"""
Pig is a multiplayer game how everyone plays it is a little bit different.
    1. Your turn roll a die.
    2. If you get anything other than 1 add to score.
    3. You can roll as many times as you want but as soon as the die shows 1, the score is set to zero.
    4. It goes on in a turn based system, as soon as someone hits a max score the game is over.
"""


def main():
    def roll() -> int:
        min_value = 1
        max_value = 6
        roll = random.randint(min_value, max_value)

        return roll

    while True:
        players = input("Enter the number of players (2-4): ")
        if players.isdigit():
            players = int(players)
            if 1 < players <= 4:
                break
            else:
                print("Must be a number between 2 and 4.")
        else:
            print("Invalid value, please enter a number between 2 and 4.")

    max_score = 50
    player_scores = [0 for _ in range(players)]

    while max(player_scores) < max_score:
        for player_index in range(players):
            print("\nPlayer number", player_index + 1, "turn has jsut started!\n")
            print("Your total score is:", player_scores[player_index], "\n")
            current_score = 0
            while True:
                should_roll = input("Would you like to roll (y)? ").lower()
                if should_roll != "y":
                    break
                value = roll()
                if value == 1:
                    print("You rolled a 1. Turn Done!")
                    current_score = 0
                    break
                else:
                    print("You rolled a", value, "!")
                    current_score += value

                print("Your current score is:", current_score)
            player_scores[player_index] += current_score
            print("Your total score is:", player_scores[player_index])
    max_scorer = max(player_scores)
    player_winning_idx = player_scores.index(max_scorer)
    print("Player number", player_winning_idx + 1, "Won!! With a score of:", max_scorer)


if __name__ == "__main__":
    main()
