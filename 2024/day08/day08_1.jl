using Combinatorics

io = open("2024/day08/input.txt", "r")

content = read(io, String)
cleanup = split(replace(content, "\r" => "", "\n" => ""), "")

field_size = 50
base = reshape(cleanup, (field_size , field_size))

# remove empty fields
different_nodes = setdiff(Set(cleanup), ["."])
unique_locations = Set()

# check all different node types
for node in different_nodes
    node_locations = findall(x -> x == node, base)
    node_combinations = collect(combinations(node_locations, 2))

    for (first, second) in node_combinations
        difference = first - second
        
        # create new anti nodes
        first_antinode = first + difference
        second_antinode = second - difference

        # check if antinodes are on the field
        for anti_node in [first_antinode, second_antinode]
            if 1 <= anti_node[1] <= field_size && 1 <= anti_node[2] <= field_size
                push!(unique_locations, anti_node)
            end
        end
    end
end

println(length(unique_locations))