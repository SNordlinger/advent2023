import re

GAME_RE = re.compile(r'Card +\d+:')


def parse_input(lines):
    cards = []
    for line in lines:
        [winning_str, num_str] = re.sub(GAME_RE, '', line).split('|')
        winning_nums = [int(n) for n in re.findall(r'\d+', winning_str)]
        numbers = [int(n) for n in re.findall(r'\d+', num_str)]
        cards.append({'winning': winning_nums, 'nums': numbers})
    return cards


def get_input():
    with open('./data/day4.txt') as input_file:
        return input_file.readlines()


def part1(data):
    points = 0
    for card in data:
        winning = set(card['winning'])
        matches = [n for n in card['nums'] if n in winning]
        if len(matches) > 0:
            game_points = 2**(len(matches) - 1)
            points += game_points

    return points


def part2(data):
    copies = 0
    reversed_cards = list(reversed(data))
    for num, card in enumerate(reversed_cards):
        winning = set(card['winning'])
        matches = [n for n in card['nums'] if n in winning]
        card_copies = 1
        for diff in range(1, len(matches) + 1):
            card_copies += reversed_cards[num - diff]['copies']
        card['copies'] = card_copies
        copies += card_copies
    return copies


def main():
    lines = get_input()
    data = parse_input(lines)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
