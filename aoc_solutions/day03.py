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
    
    def _pos_small_3_digit(self, s: str) -> list:
        return sorted(range(len(s)), key=s.__getitem__)[:3]

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
            indices_to_remove = self._pos_small_3_digit(bank)
            # Remove from string (highest indices first)
            chars = list(bank)
            for i in sorted(indices_to_remove, reverse=True):
                chars.pop(i)

            new_int = int(''.join(chars))
            power_total += new_int

        return power_total


