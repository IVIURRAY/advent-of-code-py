def add_hit(x, y, coords, matrix, seen):
    total = 0
    if seen[y][x]:
        return 0
    if seen[y][x+1]:
        return 0
    if seen[y][x-1]:
        return 0

    total += coords.get((x, y), 0)
    return total


def hits(x, y, matrix, seen, numbers):
    total = 0
    if x-1 >= 0:
        if matrix[y][x-1].isdigit():
            total += add_hit(x-1, y, numbers, matrix, seen)
            seen[y][x-1] = True
    if x+1 < len(matrix[0]):
        if matrix[y][x+1].isdigit():
            total += add_hit(x+1, y, numbers, matrix, seen)
            seen[y][x+1] = True
    if y+1 < len(matrix):
        if matrix[y+1][x].isdigit():
            total += add_hit(x, y+1, numbers, matrix, seen)
            seen[y+1][x] = True
    if y-1 >= 0:
        if matrix[y-1][x].isdigit():
            total += add_hit(x, y-1, numbers, matrix, seen)
            seen[y-1][x] = True
    if x-1 >= 0 and y-1 >= 0:
        if matrix[y-1][x-1].isdigit():
            total += add_hit(x-1, y-1, numbers, matrix, seen)
            seen[y-1][x-1] = True
    if x+1 < len(matrix[0]) and y+1 < len(matrix):
        if matrix[y+1][x+1].isdigit():
            total += add_hit(x+1, y+1, numbers, matrix, seen)
            seen[y+1][x+1] = True
    if x - 1 >= 0 and y+1 < len(matrix):
        if matrix[y+1][x-1].isdigit():
            total += add_hit(x-1, y+1, numbers, matrix, seen)
            seen[y+1][x-1] = True
    if x+1 < len(matrix[0]) and y - 1 >= 0:
        if matrix[y-1][x+1].isdigit():
            total += add_hit(x+1, y-1, numbers, matrix, seen)
            seen[y-1][x+1] = True

    print(x, y, total)
    return total


def find_numbers_coords(lines):
    """
    Loop through a line and find all the values that are digits.
    If it is a digit, then I keep track until the digit ends and then replace all the indices with that number.
    """
    coords = {}

    for iy, line in enumerate(lines):
        i = 0
        digits = ""
        indicies_seen_digit = []
        while i < len(line):
            if line[i].isdigit():
                digits = digits + line[i]
                indicies_seen_digit.append(i)
            else:
                while indicies_seen_digit:
                    ix = indicies_seen_digit.pop()
                    coords[(ix, iy)] = int(digits)
                digits = ""
            i += 1

        while indicies_seen_digit:
            ix = indicies_seen_digit.pop()
            coords[(ix, iy)] = int(digits)

    return coords


if __name__ == '__main__':
    with open('day33.txt') as f:
        seen = []
        matrix = []
        for line in f:
            seen.append([False]*len(line))
            matrix.append(list(line.strip()))

    numbers = find_numbers_coords(matrix)

    total = 0
    for y, line in enumerate(matrix):
        print(list(line))
        for x, char in enumerate(line):
            if not char.isdigit() and char != '.':
                total += hits(x, y, matrix, seen, numbers)

    print(total)
