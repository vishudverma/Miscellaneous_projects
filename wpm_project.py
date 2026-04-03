import curses
import time

"""
Learning to use the curses module to make beautiful terminal commands, or terminal text formating.
"""


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getch()


def display_text(stdscr, target: str, current: list[str], wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM:{wpm}")

    for i, char in enumerate(current):
        if char == target[i] and len(char) == 1:
            stdscr.addstr(0, i, char, curses.color_pair(1))
        if char != target[i] and len(char) == 1:
            stdscr.addstr(0, i, char, curses.color_pair(2))


def wpm_test(stdscr):
    target_text = "Hello world this is some test text for this app!"
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        time.sleep(0.25)

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:  # noqa: E722
            continue

        if len(key) == 1 and ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(key) == 1 and len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

    stdscr.addstr(2, 0, "You complete the text! Press any key to continue!")
    stdscr.getkey()


if __name__ == "__main__":
    curses.wrapper(main)
