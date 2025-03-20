def checksum(compacted : list[int]):
    return sum([i*n for i, n in enumerate(compacted) if n != -1])

def convert(raw : list[int]) -> list[int]:
    disk = []
    cur_id = 0
    for i, n in enumerate(raw):
        if i%2 == 0:
            disk += [cur_id] * n
            cur_id+=1
        else:
            disk += [-1] * n
    return disk

def move(col, trgt_start, trgt_end, src_start, src_end):
    col[trgt_start:trgt_end] = col[src_start:src_end]
    col[src_start:src_end] = [-1]*(src_end-src_start)

def empty_spots(converted: list[int]):
    spots = []
    (start, end) = None, None
    for (i, x) in enumerate(converted):
        if x == -1 and start is None:
            start = i
        if x != -1 and start is not None:
            end = i
            spots.append((start, end))
            start = None
            end = None
    return spots

def compact(converted : list[int]) -> list[int]:
    uncompacted = converted.copy()

    clear_locs = empty_spots(uncompacted)
    unique_ids = sorted(list(set(uncompacted).difference(set([-1]))), reverse=True)

    for identifier in unique_ids:
        #find source block start and end
        filtered = list(map(lambda x: x[0], filter(lambda x: x[1] == identifier, enumerate(uncompacted))))
        min_id_idx = min(filtered)
        max_id_idx = max(filtered)

        #source block size
        seq_size = max_id_idx - min_id_idx + 1

        # dont iterate through copy for performance reasons
        for tup in clear_locs:
            (a, b) = tup[0], tup[1]

            # check if block size fits and target is to the left of the source
            if (b - a) >= seq_size and b <= min_id_idx:
                # move block to the left
                move(uncompacted, a, a+seq_size, min_id_idx, min_id_idx+seq_size)
                
                # update empty block locations 
                # (remove if size fits perfectly; update if space is left)
                idx = clear_locs.index(tup)
                if (b - a) > seq_size:
                    clear_locs[idx] = (a+seq_size, b)
                else:
                    # we directly stop iterating after removing so modifying is ok
                    clear_locs.remove(tup)
                break
    return uncompacted
        
with open("2024/day09/input.txt") as puzzle:
    contents = list(map(int, puzzle.read()))

    converted_disk = convert(contents)
    empty_locs = empty_spots(converted_disk)

    compressed = compact(converted_disk)
    print(checksum(compressed))
    