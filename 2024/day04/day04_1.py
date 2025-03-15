def check_direction(grid: list[list[str]], w0: int, wn: int, hn: int, y_step: int, x_step: int, query: str) -> int:
    found = 0
    for w in range(w0, wn):
        for h in range(hn):
            subject = "".join([grid[h + y_step * i][w + x_step * i] for i in range(len(query))])
            if subject == query or subject == query[::-1]:
                found += 1
    return found

with open("2024/day04/input.txt", mode="r", encoding="utf8") as puzzle:
    grid = list(map(list, puzzle.read().splitlines()))

    width, height = (len(grid[0]), len(grid))
    word, length = ("XMAS", len("XMAS"))

    x_count = check_direction(grid, 0, width - length + 1, height, 0, 1, "XMAS")
    y_count = check_direction(grid, 0, width, height - length + 1, 1, 0, "XMAS")
    xy_lr_count = check_direction(grid, 0, width - length + 1, height - length + 1, 1, 1, "XMAS")
    xyn_rl_count = check_direction(grid, length - 1, width, height - length + 1, 1, -1, "XMAS")

    total = x_count + y_count + xy_lr_count + xyn_rl_count

    print(total)