import re

def extract_multiplication(instruction : str) -> int:
    p1, p2 = map(int, instruction.replace("mul(", "").replace(")", "").split(","))

    return p1 * p2

def toggle_multiplication(instruction_set : list[str]) -> int:
    toggled = True
    total = 0
    for instruction in instruction_set:
        if instruction == "do()":
            toggled = True
        elif instruction == "don't()":
            toggled = False
        elif toggled:
            total += extract_multiplication(instruction)
    return total

with open("2024/day03/input.txt", mode="r", encoding="utf8") as puzzle:
    instructions = puzzle.read()

    matches = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))", instructions)

    print(matches)
    print(toggle_multiplication(matches))

