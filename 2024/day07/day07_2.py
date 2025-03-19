from itertools import product

def has_possible_solution(result, operands):
    # brute force all 3^{n-1} possibilities for placing +, *, ||
    for p in product(["+", "*", "||"], repeat=len(operands)-1):
        acc = operands[0]
        for i in range(1, len(operands)):
            if p[i-1] == "+":
                acc += operands[i]
            if p[i-1] == "*":
                acc *= operands[i]
            if p[i-1] == "||":
                acc = int(str(acc) + str(operands[i]))
        if acc == result:
            return True
    return False

def find_total_solutions(equations : dict[int, list[int]]):
    return sum([key for (key, operands) in equations.items() if has_possible_solution(key, operands)])


with open("2024/day07/input.txt", mode="r", encoding="utf8") as puzzle:
    lines = puzzle.read().splitlines()
    parts =  list(map(lambda line : tuple(line.split(":")), lines))

    equations = {int(result) : list(map(int, operands.strip().split(" "))) for (result, operands) in parts}
    
    print(find_total_solutions(equations))