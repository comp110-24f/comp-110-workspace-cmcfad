"""A program to plan a teaparty"""

__author__: str = "730764947"


def main_planner(guests: int) -> None:
    """Calls all functions and produces a printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")  # convert guests to str
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # uses tea_bags #converts to str bc int cant use int in str
    print("Treats: " + str(treats(people=guests)))  # same as above
    print(
        "Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests)))
    )  # uses both functions to get info


def tea_bags(people: int) -> int:
    """Number of people and calculates the tea bags needed"""
    return people * 2  # num ppl times 2


def treats(people: int) -> int:  # takes num tea bags multiplied by 1.5
    """Number of treats needed for the guests"""  # b/c 1.5 per cup of tea
    return int(tea_bags(people=people) * 1.5)  # uses int to convert float to int


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates cost of party"""
    return (tea_count * 0.5) + (
        treat_count * 0.75
    )  # provides the cost based on idv components


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
