"""A wordle program"""

__author__ = "730764947"
# Remember to comment code


def input_guess(secret_word_len: int) -> str:
    """Checks to make sure word is correct len"""
    guess_word: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # uses secret word len and changes each time
    while len(guess_word) != secret_word_len:  # changes based on this variable
        guess_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess_word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Is char guess in the word?"""
    assert len(char_guess) == 1  # throws error if not
    index: int = 0
    while index < len(secret_word):  # is this true?
        if secret_word[index] == char_guess:  # if it is return true
            return True
        index += 1  # and add index
    return False  # if through whole loop and not found, return false


def emojified(guess: str, secret: str) -> str:
    """Iterates through guess and assigns emojis accordingly"""
    assert len(guess) == len(secret)
    index: int = 0
    box_output: str = ""  # set an empty str to concat to
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index < len(secret):  # go through entire guess
        if guess[index] == secret[index]:  # if correct green box
            box_output += GREEN_BOX
        elif (
            contains_char(secret, guess[index]) is True
        ):  # if it is in it somewhere yellow box
            box_output += YELLOW_BOX  # uses previously made contains_chrar
        else:
            box_output += WHITE_BOX  # if none of those white box
        index += 1
    return box_output  # return the str


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    turn: int = 1
    won: bool = False
    while turn <= 6 and won is False:  # uses and statment bc both have to be true
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))  # guess variable is the return of input_guess
        print(emojified(guess, secret))  # runs this fn with guess and secret
        if guess == secret:
            won = True
        turn += 1
    if won is True:  # kept throwing an error if I used == or = and wanted to use is
        print(f"You won in {turn - 1}/6 turns!")  # have to do -1 bc loop will add 1
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
