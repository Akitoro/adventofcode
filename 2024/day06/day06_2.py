def simulate_path(position, facing, room):
    path = set()
    cur_pos = position
    cur_face = facing
    while (cur_pos, cur_face) not in path:
        path.add((cur_pos, cur_face))
        next_pos = (l_x, l_y) = (cur_pos[0] + cur_face[0], cur_pos[1] + cur_face[1])

        if not(0 <= l_y < len(room) and 0 <= l_x < len(room[0])):
            return path, False
        
        if room[l_y][l_x] == "#":
            cur_face = turn_right(cur_face)
        elif room[l_y][l_x] == "." or room[l_y][l_x] == "^":
            cur_pos = next_pos
    return path, True

def turn_right(facing):
    return (-1 * (facing[0] * 0 + facing[1] * 1), -1 * (facing[0] * -1 + facing[1] * 0))
    

with open("2024/day06/input.txt") as puzzle:
    room = list(map(list, puzzle.read().splitlines()))

    (height, width) = len(room), len(room[0])

    guard_position = [ (x,y) for x in range(width) for y in range(height) if room[y][x] == "^"][0]

    configurations = set(map(lambda x: x[0], simulate_path(guard_position, (0, -1), room)[0]))
    
    obstacle_positions = set()
    for i, (pos_x, pos_y) in enumerate(configurations):
        old = room[pos_y][pos_x]
        room[pos_y][pos_x] = "#"

        simulation = simulate_path(guard_position, (0, -1), room)
        if simulation[1]:
            obstacle_positions.add((pos_x, pos_y))
        room[pos_y][pos_x] = old
    print(len(obstacle_positions))