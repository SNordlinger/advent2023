import re


def parse_input(lines):
    data = {'numbers': [], 'symbols': []}
    for y, line in enumerate(lines):
        matches = re.finditer(r'[^\d\.\n]', line)
        for match in matches:
            data['symbols'].append({
                'symbol': match.group(0),
                'y': y,
                'x': match.start(),
                'nums': []
            })
    for y, line in enumerate(lines):
        number_matches = re.finditer(r'\d+', line)
        symbols = [
            s for s in data['symbols'] if s['y'] >= y - 1 and s['y'] <= y + 1
        ]
        for match in number_matches:
            adjacent = [
                s for s in symbols
                if s['x'] >= match.start() - 1 and s['x'] <= match.end()
            ]
            num_info = {
                'num': int(match.group(0)),
                'x': match.start(),
                'y': y,
                'end': match.end() - 1,
                'is_part': len(adjacent) > 0
            }
            for adj in adjacent:
                adj['nums'].append(num_info)
            data['numbers'].append(num_info)
    return data


def get_input():
    with open('./data/day3.txt') as input_file:
        return input_file.readlines()


def part1(data):
    return sum(n['num'] for n in data['numbers'] if n['is_part'])


def part2(data):
    gears = (s for s in data['symbols']
             if s['symbol'] == '*' and len(s['nums']) == 2)
    ratios = (g['nums'][0]['num'] * g['nums'][1]['num'] for g in gears)
    return sum(ratios)


def main():
    lines = get_input()
    data = parse_input(lines)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
