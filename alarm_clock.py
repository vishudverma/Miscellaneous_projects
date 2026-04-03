"""Making an alarm clock and using it for daily"""

import pygame
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(
            f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}"
        )

        if time_elapsed == seconds:
            pygame.mixer.init()
            pygame.mixer.music.load("alarm.wav")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue


def main():
    minutes = int(input("How many minutes to wait: "))
    seconds = int(input("How many seconds to wait: "))
    total_seconds = minutes * 60 + seconds
    alarm(total_seconds)


if __name__ == "__main__":
    main()
