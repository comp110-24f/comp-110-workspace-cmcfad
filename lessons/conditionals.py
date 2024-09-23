def wake_up(alarm: bool) -> str:
    """Return a message based off if alarm is going off"""
    if alarm is True:
        return "Wake up! Go to class"
    else:
        return "Keep sleeping"


"""Practice question"""


def check_first_letter(word: str, letter: str) -> str:
    """Check if letter is first character in word"""
    if word[0] == letter:
        return "Match!"
    else:
        return "No match"


print(check_first_letter(word="happy", letter="s"))
