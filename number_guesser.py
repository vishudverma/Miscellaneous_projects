import random


def main():
    top_of_range = input("Type a number: ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            print("Please type a number larger than zero next time.")
            quit()
    else:
        print("Please type in a number next time.")
        quit()

    random_number = random.randint(0, top_of_range)
    guesses = 0

    while True:
        guesses += 1
        user_guess = input("Make a guess: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please type in a number next time.")
            continue

        if user_guess == random_number:
            print("You guessed the correct number.")
            print(f"Your got it in {guesses} guesses.")
            break
        elif user_guess < random_number:
            print("You were short of it, try a bigger number.")
        else:
            print("You were way big, try a smaller number.")


if __name__ == "__main__":
    main()
