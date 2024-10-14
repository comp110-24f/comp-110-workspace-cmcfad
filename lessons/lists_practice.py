"""Practice with lists"""

my_numbers: list[float] = list()  # or = []


# Add item to list
my_numbers.append(1.5)  # one at a time


game_points: list[int] = [102, 86, 94]
# print(game_points[2])
game_points[1] = 72
game_points.append(86)
print(game_points)

# Length
# print(len(game_points))

game_points.pop(1)
print(game_points)


# Write a fn called display
# Input: list[int]
# Return Value: None
# Loop over input and print every value
# Try calling it on game points


def display(Input: list[int]) -> None:
    index: int = 0
    while index < len(Input):
        print(Input[index])
        index += 1


display(Input=game_points)
