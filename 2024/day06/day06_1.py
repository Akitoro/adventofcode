def simulate_path(position, facing, room):
    path = []
    cur_pos = position
    cur_face = facing
    while (cur_pos, cur_face) not in path:
        path.append((cur_pos, cur_face))
        next_pos = (l_x, l_y) = tuple(sum(x) for x in zip(cur_pos, cur_face))

        if not(0 <= l_y < len(room) and 0 <= l_x < len(room[0])):
            return path
        
        if room[l_y][l_x] == "#":
            cur_face = tuple(turn_right(cur_face))
        elif room[l_y][l_x] == "." or room[l_y][l_x] == "^":
            cur_pos = next_pos
    return path

def turn_right(facing):
    # Drehmatrix um -90 Grad anwenden
    #  0 1
    # -1 0
    return (-1 * (facing[0] * 0 + facing[1] * 1), -1 * (facing[0] * -1 + facing[1] * 0))
    

with open("2024/day06/input.txt") as puzzle:
    room = list(map(list, puzzle.read().splitlines()))

    (height, width) = len(room), len(room[0])

    guard_position = [ (x,y) for x in range(width) for y in range(height) if room[y][x] == "^"][0]


    path = simulate_path(guard_position, (0, -1), room)
    unique_positions = set(map(lambda x: x[0], path))

    print(len(unique_positions))