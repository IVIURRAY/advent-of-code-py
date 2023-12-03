def find_coords_of_symbols():
    coords = []

    return coords

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

    return coords


if __name__ == '__main__':
    with open('day3.txt') as f:
        matrix = []
        for line in f:
            matrix.append(list(line.strip()))
        print(matrix)
        numbers = find_numbers_coords([['4', '6', '7', '.', '.', '1', '1', '4', '.', '.']])
        print(numbers)
