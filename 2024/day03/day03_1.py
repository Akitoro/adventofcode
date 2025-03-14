import re

def extract_multiplication(instruction : str) -> int:
    p1, p2 = map(int, instruction.replace("mul(", "").replace(")", "").split(","))

    return p1 * p2

with open("2024/day03/input.txt", mode="r", encoding="utf8") as puzzle:
    instructions = puzzle.read()

    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", instructions)

    total = sum(map(extract_multiplication, matches))

    print(total)

