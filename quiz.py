def main():
    print("Welcome to my computer quiz!")
    playing = input("Do you want to play the game?\n")
    if playing.lower() != "yes":
        quit()
    print("Okay! lets play :)")
    score = 0

    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("What does GPU stand for? ")
    if answer.lower() == "graphical processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("What does RAM stand for? ")
    if answer.lower() == "random access memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("What does PSU stand for? ")
    if answer.lower() == "power supply unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print(f"You have got {score} questions correct!")
    print(f"You have got {score / 4 * 100} % questions correct!")


if __name__ == "__main__":
    main()
