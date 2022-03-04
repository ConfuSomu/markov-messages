# This takes for granted that the terminal used supports ANSI escape codes. Some terminals do not, but we do not check.
class ANSI:
    reset = '\033[0m'
    underline = '\033[4m'