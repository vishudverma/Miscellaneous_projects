import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = [
    "red",
    "green",
    "blue",
    "orange",
    "yellow",
    "black",
    "purple",
    "pink",
    "brown",
    "cyan",
]


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle racing adventure!")


def get_number_of_racers() -> int:
    racers = 0
    while True:
        racers = input("How many tutles do you want to put in the race (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric...... Try Again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number is not in range 2-10, try again!")


def create_turtles(colors):
    turtles = []
    x_coordinate = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * x_coordinate, -HEIGHT // 2 + 30)
        turtles.append(racer)

    return turtles


def race(colors):
    racers = create_turtles(colors)
    while True:
        for racer in racers:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            _, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[racers.index(racer)]


def main():
    racers = get_number_of_racers()
    init_turtle()
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    color = race(colors)
    print(f"The winner is {color}")
    time.sleep(5)


if __name__ == "__main__":
    main()
