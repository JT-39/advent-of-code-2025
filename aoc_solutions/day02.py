# day02.py
from .base_day import BaseDay

class Day02(BaseDay):
    """Day 2: Product ID repeated halves / splits."""

    @staticmethod
    def split_in_n(word: str, n: int):
        part_len = len(word) // n
        return [word[i*part_len:(i+1)*part_len] for i in range(n)]

    @staticmethod
    def has_repeated_halves(pid: int) -> bool:
        s = str(pid)
        mid = len(s) // 2
        return s[:mid] == s[mid:]

    @staticmethod
    def has_any_repeated_split(pid: int) -> bool:
        s = str(pid)
        length = len(s)
        for n_parts in range(2, length+1):
            if length % n_parts != 0:
                continue
            part_len = length // n_parts
            first_part = s[:part_len]
            if all(s[i*part_len:(i+1)*part_len] == first_part for i in range(n_parts)):
                return True
        return False

    def _parse_ranges(self):
        """Parse input data like '2121212118-2121212124' into integer tuples."""
        ranges = []
        for line in self.data:
            line = line.strip()
            if line:
                low, high = map(int, line.split("-"))
                ranges.append((low, high))
        return ranges

    def solve_part1(self):
        total = 0
        for low, high in self._parse_ranges():
            for pid in range(low, high+1):
                if self.has_repeated_halves(pid):
                    total += pid
        return total

    def solve_part2(self):
        total = 0
        for low, high in self._parse_ranges():
            for pid in range(low, high+1):
                if self.has_any_repeated_split(pid):
                    total += pid
        return total
