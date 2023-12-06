import re

SEED_RE = re.compile(r'seeds: (\d[\d ]*\d)')
CONVERSION_RE = re.compile(r'([a-z]+)-to-([a-z]+) map:\n([\d ]+\n)+')

def parse_input(text):
    pass

def parse_seeds(text):
    seed_match = re.match(SEED_RE, text)
    seed_text = seed_match.group(1)
    seed_nums = [int(n) for n in seed_text.split(' ')
    return seed_nums


def get_input():
    with open('./data/day5.txt') as input_file:
        return input_file.read()


def part1(data):
    pass


def part2(data):
    pass


def main():
    lines = get_input()
    data = parse_input(lines)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
