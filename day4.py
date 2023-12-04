if __name__ == '__main__':
    result = 0
    with open('day4.txt') as f:
        for line in f:
            game_id, game = line.split(':')
            winning, numbers = game.split("|")
            winning = winning.strip().split()
            numbers = numbers.strip().split()

            total = 0
            for number in numbers:
                if number in winning:
                    if total == 0:
                        total = 1
                    else:
                        total *= 2

            result += total
            print(game_id, total)

        print(result)