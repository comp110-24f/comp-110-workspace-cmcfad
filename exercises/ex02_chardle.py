"""EX02 - Chardle - A step toward Wordle."""

__author__ = "730764947"

# Remeber to comment code!


def input_word() -> str:
    five_char_word: str = input("Enter a 5-character word: ")
    if int(len(five_char_word)) != 5:  # not equal five so return error
        print("Error: Word must contain 5 characters.")
        exit()
    return five_char_word


def input_letter() -> str:
    single_letter: str = input("Enter a single character: ")
    if int(len(single_letter)) != 1:  # same as above checks for 1 char, is len = 1
        print("Error: Character must be a single character.")
        exit()
    return single_letter


def contains_char(word: str, letter: str) -> None:
    count: int = 0  # for the count of instances
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:  # checks each index to see if letter is there
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    if count == 1:
        print("1 instance of " + letter + " found in " + word)
    if count >= 2:  # 2 and greater
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
