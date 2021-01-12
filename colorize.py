from colorama import init, Fore

init()


def colorize(string, color):
    """
    Returns a string colored with the selected color.
    Available colors: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
    """
    return str(getattr(Fore, color.upper()) + str(string) + Fore.RESET)
