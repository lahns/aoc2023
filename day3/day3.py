def find_adjacent_coordinates(i, j, current_number, special_coord):
    current_number.append(grid[i][j])
    special_coord[0] = special_coord[0] or find_special_coordinate(i, j)
    grid[i][j] = "."
    j += 1
    if j < cols and grid[i][j].isdigit():
        find_adjacent_coordinates(i, j, current_number, special_coord)
    return current_number, special_coord

def find_special_coordinate(i, j):
    for delta_row, delta_col in (1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1):
        r = delta_row + i
        c = delta_col + j
        if 0 <= r < rows and 0 <= c < cols and not grid[r][c].isdigit() and grid[r][c] != ".":
            return (r, c)


with open("input.txt") as file:
    input_data = file.read().split()
    grid = [list(row) for row in input_data]

rows = len(grid)
cols = len(grid[0])
symbol_coordinates = {}
part_sum = 0
gear_ratio_sum = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c].isdigit():
            current_number, special_coord = find_adjacent_coordinates(r, c, [], [()])
            num = int("".join(current_number))
            special_coord = special_coord[0]
            if special_coord:
                part_sum += num
                symbol_coordinates.setdefault(special_coord, []).append(num)

for coord in symbol_coordinates:
    nums_at_coord = symbol_coordinates[coord]
    if len(nums_at_coord) == 2:
        gear_ratio_sum += (nums_at_coord[0] * nums_at_coord[1])

print("part numbers:", part_sum)
print("gear ratios:", gear_ratio_sum)
print(symbol_coordinates, special_coord)