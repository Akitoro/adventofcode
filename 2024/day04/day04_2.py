def check_square(grid: list[list[str]], query: list[list[str]]) -> int:
    preturned = [
        query,
        rotate(query),
        rotate(rotate(query)),
        rotate(rotate(rotate(query)))
    ]

    query_width, query_height = (len(query[0]), len(query))
    grid_width, grid_height = (len(grid[0]), len(grid))

    found = 0
    for w in range(grid_width - query_width + 1):
        for h in range(grid_height - query_height + 1):
            selection = list(map(lambda x: x[w:w+query_width], grid[h:h+query_height]))

            # check all turned lists
            for rotated in preturned:
                if (check_match(selection, rotated)):
                    found += 1
    return found


def check_match(selection: list[list[str]], query: list[list[str]]) -> bool:
    for i, y in enumerate(selection):
        for j, x in enumerate(y):
            if not (query[i][j] == "_" or x == query[i][j]):
                return False
    return True

def rotate(arr):
    return list(zip(*arr[::-1]))


with open("2024/day04/input.txt", mode="r", encoding="utf8") as puzzle:
    grid = list(map(list, puzzle.read().splitlines()))

    query = [
        ["M", "_", "S"],
        ["_", "A", "_"],
        ["M", "_", "S"]
    ]

    print(check_square(grid, query))
