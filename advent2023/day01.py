import re

WORD_RE = re.compile(r'one|two|three|four|five|six|seven|eight|nine')


def get_input():
    with open('./data/day1.txt') as input_file:
        return input_file.readlines()


def search_for_digit(text):
    digit_match = re.search(r'\d', text)
    if digit_match:
        return digit_match.group(0)

    digit_words = [
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
    ]
    for num, word in enumerate(digit_words, start=1):
        if text.endswith(word) or text.startswith(word):
            return str(num)

    return None


def part1(lines):
    count = 0
    for line in lines:
        digits = re.sub(r'\D+', '', line)
        num = int(f'{digits[0]}{digits[len(digits) - 1]}')
        count += num
    return count


def part2(lines):
    count = 0
    for line in lines:
        first = next(digit for end in range(0, len(line))
                     if (digit := search_for_digit(line[:end])) is not None)
        last = next(digit for start in range(len(line), -1, -1)
                    if (digit := search_for_digit(line[start:])) is not None)
        num = int(f'{first}{last}')
        count += num
    return count


def main():
    lines = get_input()
    part1_result = part1(lines)
    print(f'Part 1: {part1_result}')

    part2_result = part2(lines)
    print(f'Part 2: {part2_result}')


if __name__ == '__main__':
    main()
