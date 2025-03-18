from functools import cmp_to_key

def order_check(check, rules):
    relevant_order = list(filter(lambda t : t[0] in check and t[1] in check, rules))

    def compare(x : int, y: int):
        if (x,y) in rules:
            return -1
        else:
            return 1
        
    return sorted(check, key=cmp_to_key(compare))

with open("2024/day05/input.txt") as puzzle:
    instructions = puzzle.read().splitlines()
    sep_index = instructions.index('')

    order_rules = set(map(lambda s : tuple(map(int, s.split("|"))), instructions[:sep_index]))
    order_checks = list((map(lambda s: list(map(int, s.split(","))), instructions[sep_index+1:])))

    total = 0
    for check in order_checks:
        
        implied_order = set(zip(check, check[1:]))
        if not implied_order.issubset(order_rules):
            next_order = order_check(check, order_rules)
            total += next_order[len(next_order)//2]

    print(total)