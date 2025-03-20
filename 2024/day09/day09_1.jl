function checksum(compacted) :: Int
    check = 0
    for i in eachindex(compacted)
        if compacted[i] != -1
            check += (i-1) * compacted[i]
        end
    end
    return check
end

function convertdiskmap(diskmap :: Array{Int})
    disk::Array{Int} = []
    id = 0
    for (i, x) in enumerate(diskmap)
        if i % 2 == 1
            disk = vcat(disk, repeat([id], x))
            id += 1
        else
            disk = vcat(disk, repeat([-1], x))
        end
    end
    return disk
end

function compact(uncompacted)
    for i in length(uncompacted):-1:1
        if uncompacted[i] != -1
            pos = findfirst(x -> x == -1, uncompacted)[1]
            if isnothing(pos) || pos > i
                return uncompacted
            end
            uncompacted[pos] = uncompacted[i]
            uncompacted[i] = -1
        end
    end
    return uncompacted
end

io = open("2024/day09/input.txt", "r")
content = map(x -> parse(Int, x), collect(replace(read(io, String), "\r" => "", "\n" => "")))

diskmap = convertdiskmap(content)
fragmented = compact(diskmap)

println(checksum(fragmented))