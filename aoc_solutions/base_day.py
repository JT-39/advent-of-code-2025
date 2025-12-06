# base_day.py

from pathlib import Path

class BaseDay:
    """Base class for Advent of Code days."""
    
    def __init__(self, day_number: int, data_dir="data"):
        self.day_number = day_number
        self.data_dir = Path(data_dir)
        self.filepath = self.data_dir / f"day{day_number:02}.txt"
        self.data = self._read_data()
    
    def _read_data(self):
        """Read input file as a list of stripped lines."""
        with open(self.filepath, "r") as f:
            return [line.strip() for line in f.readlines()]
    
    def solve_part1(self):
        """Override this method for Part 1 solution."""
        raise NotImplementedError
    
    def solve_part2(self):
        """Override this method for Part 2 solution."""
        raise NotImplementedError
