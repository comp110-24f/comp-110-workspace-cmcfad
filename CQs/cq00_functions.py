"""Challenge Question 00"""

__author__ = "730764947"


def mimic(message: str) -> str:
    """Take what you say and repeat it"""
    return message


def main() -> None:
    """Prints result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
