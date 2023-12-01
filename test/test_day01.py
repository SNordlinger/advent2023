from advent2023.day01 import part1, part2

def test_part1():
    sample_input = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet""".splitlines()
    assert part1(sample_input) == 142


def test_part2():
    sample_input = """two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen""".splitlines()
    assert part2(sample_input) == 281
