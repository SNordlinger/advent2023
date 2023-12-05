from advent2023.day03 import part1, parse_input, part2

sample_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".splitlines()


def test_part1():
    data = parse_input(sample_input)
    assert part1(data) == 4361


def test_part2():
    data = parse_input(sample_input)
    assert part2(data) == 467835
