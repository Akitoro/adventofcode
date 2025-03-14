def check_report(report: list[int]) -> bool:
    sorted_report = sorted(report)
    # check if sorted
    if (sorted_report != report and sorted_report[::-1] != report):
        return False
    # check if distances are correct
    for x, y in zip(report, report[1:]):
        if not (1 <= abs(x-y) <= 3):
            return False
    return True

with open("2024/day02/input.txt", mode="r", encoding="utf8") as puzzle:
    reports = list(map(lambda x: list(map(int, x.split(" "))),
                   puzzle.read().splitlines()))

    print(list(map(check_report, reports)).count(True))
