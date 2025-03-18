with open("2024/day05/input.txt") as puzzle:
    instructions = puzzle.read().splitlines()
    sep_index = instructions.index('')

    order_rules = set(map(lambda s : tuple(map(int, s.split("|"))), instructions[:sep_index]))
    order_checks = list((map(lambda s: list(map(int, s.split(","))), instructions[sep_index+1:])))

    total = 0
    for check in order_checks:
        
        implied_order = set(zip(check, check[1:]))
        if implied_order.issubset(order_rules):
            total += check[len(check)//2]

    print(total)