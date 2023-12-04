if __name__ == '__main__':
    result = 0
    copies = []
    cards = {}

    with open('day4.txt') as f:
        for i, line in enumerate(f, start=1):
            game_id, game = line.split(':')
            winning, numbers = game.split("|")
            winning = winning.strip().split()
            numbers = numbers.strip().split()

            count = 0
            result += 1
            for number in numbers:

                if number in winning:
                    count += 1

            print(game_id, count)
            cards[i] = {'id': i, 'winning': winning, 'numbers': numbers, 'won': count}

        for game_id, game in cards.items():
            count = game['won']
            while count > 0:
                result += 1
                print(f'{game_id}: Adding {game_id + count} to copies')
                copies.append(cards[game_id + count])
                count -= 1

        while copies:
            game = copies.pop(0)
            game_id = game['id']
            count = game['won']

            while count > 0:
                result += 1
                print(f'{game_id}: Adding {game_id + count} to copies')
                copies.append(cards[game_id + count])
                count -= 1


        print(result)
