from aoc_solutions.base_day import BaseDay

# day03 = BaseDay(day_number=3, delimiter="\n")

# power = 0
# for bank in day03.data:
#     max_pos = max(range(len(bank) - 1), key=bank.__getitem__)
#     max_pos2 = max(range(max_pos + 1, len(bank)), key=bank.__getitem__)
#     digit_01 = bank[max_pos]
#     digit_02 = bank[max_pos2]
#     power += int(digit_01 + digit_02)

# print(f"Answer to Day 3 part 1: {power}")

class Day03(BaseDay):
    """Day 3: Calculate Power"""

    def _pos_first_max_digit(self, s: str) -> int:
        return max(range(len(s) - 1), key=s.__getitem__)

    def _pos_second_max_digit(self, s: str, first_pos: int) -> int:
        return max(range(first_pos + 1, len(s)), key=s.__getitem__)

    def _concat_digits(self, s: str, i: int, j: int) -> int:
        return int(s[i] + s[j])
    
    def _max_joltage(self, bank: str, num_digits: int = 12) -> int:
        stack = []
        n = len(bank)
        
        for i, d in enumerate(bank):
            # While we can remove a digit to make number bigger
            while stack and d > stack[-1] and len(stack) + (n - i) > num_digits:
                stack.pop()
            if len(stack) < num_digits:
                stack.append(d)
        
        return int(''.join(stack))

    def solve_part1(self) -> int:
        power_total = 0

        for bank in self.data:
            first = self._pos_first_max_digit(bank)
            second = self._pos_second_max_digit(bank, first)
            power_total += self._concat_digits(bank, first, second)

        return power_total
    
    def solve_part2(self):
        power_total = 0

        for bank in self.data:
            largest_int = self._max_joltage(bank)
            power_total += largest_int

        return power_total


