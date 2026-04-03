def main():
    name = input("What is your name? ")
    print(f"Welcome {name} to this adventure!")

    answer = input(
        "You have come on a dirt road, it has come to an end and you can go left or right. Which way do you want to go? "
    ).lower()
    if answer == "left":
        answer = input(
            "You come to a river, you can walk around it or swim across! Type walk to walk around and swim to swim across: "
        ).lower()
        if answer == "swim":
            print("There was a crocodile in the river you are dead.")
        elif answer == "walk":
            print("You walked for many miles ran out of water and died.")
    elif answer == "right":
        answer = input(
            "You come to a bridge, it looks wobbly do you want to cross or head back (cross/back)"
        ).lower()
        if answer == "cross":
            answer = input(
                "You cross the bridge and meet a stranger. Do you talk to them? (yes/no): "
            ).lower()
            if answer == "yes":
                print("You talk to the stranger, they give you gold. YOU WIN !!")
            elif answer == "no":
                print("You offended the stranger by ignoring them and they killed you.")
            else:
                print("Not a valid option. You lose.")
        elif answer == "back":
            print("You go back and loose.")
    else:
        print("Not a valid option. You lose.")


if __name__ == "__main__":
    main()
