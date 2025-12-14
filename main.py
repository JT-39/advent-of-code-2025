# main.py
from aoc_solutions.day02 import Day02
from aoc_solutions.day03 import Day03

# Day 2
day02 = Day02(day_number=2, delimiter=",")
print("Day 2 - Part 1:", day02.solve_part1())
print("Day 2 - Part 2:", day02.solve_part2())

# Day 3
day03 = Day03(day_number=3, delimiter="\n")
print("Day 3 - Part 1:", day03.solve_part1())