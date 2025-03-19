using Combinatorics

io = open("2024/day08/input.txt", "r")

content = read(io, String)
cleanup = split(replace(content, "\r" => "", "\n" => ""), "")

field_size = 50
base = reshape(cleanup, (field_size , field_size))

# remove empty fields
different_nodes = setdiff(Set(cleanup), ["."])
unique_locations = Set()

function isonfield(anti_node)
    return 1 <= anti_node[1] <= field_size && 1 <= anti_node[2] <= field_size
end

function calculate_antinodes(outgoing_node, node_step)
    cur_anti_node = outgoing_node
    while isonfield(cur_anti_node)
        push!(unique_locations, cur_anti_node)
        cur_anti_node += node_step
    end
end

# check all different node types
for node in different_nodes
    node_locations = findall(x -> x == node, base)
    node_combinations = collect(combinations(node_locations, 2))

    for (first, second) in node_combinations
        difference = first - second

        calculate_antinodes(first, difference)
        calculate_antinodes(second, - difference)
    end
end

println(length(unique_locations))