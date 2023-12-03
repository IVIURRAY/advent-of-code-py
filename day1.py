def process_line(line):
    first_digit = None
    last_digit = None
    my_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
               "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    first_pointer = 0
    last_pointer = len(line)
    while first_pointer < len(line):
        if line[first_pointer].isdigit():
            first_digit = line[first_pointer]
            break
        for key, value in my_dict.items():
            if line[first_pointer:first_pointer + len(key)] == key:
                if first_digit is None:
                    first_digit = value

        first_pointer += 1

    while last_pointer >= 0:
        if line[last_pointer - 1].isdigit():
            if last_digit is None:
                last_digit = line[last_pointer - 1]
        for key, value in my_dict.items():
            if line[last_pointer - len(key):last_pointer] == key:
                if last_digit is None:
                    last_digit = value

        last_pointer -= 1

    if first_digit is None and last_digit:
        first_digit = last_digit
    if last_digit is None and first_digit:
        last_digit = first_digit

    print(line, first_digit, last_digit)
    return first_digit + last_digit



if __name__ == '__main__':
    process_line("eightwothree")
    # process_line("71six14rkdhdszbfz")
    # process_line("abctwoabc")
    # process_line("3twoabc")
    # process_line("three4abc")
    # process_line("tsadfabc4")
    # process_line("tsadfabctwo")
    # process_line("jrnf3")

    total_sum = 0
    with open('day1.txt') as f:
        for line in f:
            result = process_line(line)
            result = int(result[0] + result[-1])
            total_sum += result
    print(total_sum)

    assert 53389 == total_sum
