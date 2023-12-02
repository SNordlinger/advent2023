import re
import itertools

GAME_RE = re.compile(r'Game \d+: ')


def get_input():
    with open('./data/day2.txt') as input_file:
        return input_file.readlines()


def parse_input(lines):
    games = []
    for line in lines:
        stripped_line = re.sub(GAME_RE, '', line.strip())
        game = [parse_subset(text) for text in stripped_line.split('; ')]
        games.append(game)
    return games


def parse_subset(subset_text):
    subset = {'red': 0, 'blue': 0, 'green': 0}
    for entry in subset_text.split(', '):
        (count, color) = parse_entry(entry)
        subset[color] = count
    return subset


def parse_entry(entry_text):
    parts = entry_text.split(' ')
    return (int(parts[0]), parts[1])


def check_game(game):
    return all(sub['red'] <= 12 and sub['green'] <= 13 and sub['blue'] <= 14
               for sub in game)


def min_cube_power(game):
    mins = {'red': 0, 'blue': 0, 'green': 0}
    for sub in game:
        mins['red'] = max(mins['red'], sub['red'])
        mins['blue'] = max(mins['blue'], sub['blue'])
        mins['green'] = max(mins['green'], sub['green'])
    return mins['red'] * mins['blue'] * mins['green']


def part1(games):
    valid_sum = 0
    for num, game in enumerate(games, start=1):
        if check_game(game):
            valid_sum += num

    return valid_sum


def part2(games):
    return sum(min_cube_power(game) for game in games)


def main():
    lines = get_input()
    games = parse_input(lines)
    print(f'Part 1: {part1(games)}')
    print(f'Part 2: {part2(games)}')


if __name__ == '__main__':
    main()
