class ProductIDProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.ranges = self._read_ranges()
    
    def _read_ranges(self):
        """Read the file and parse ranges into list of integer tuples."""
        with open(self.filepath, "r") as f:
            raw_ranges = f.read().split(",")
        raw_ranges = [r.strip() for r in raw_ranges]
        ranges = [tuple(map(int, r.split("-"))) for r in raw_ranges]
        return ranges

    @staticmethod
    def split_in_n(word, n):
        """Split a string into n equal parts (length must be divisible)."""
        part_len = len(word) // n
        return [word[i*part_len:(i+1)*part_len] for i in range(n)]

    @staticmethod
    def has_repeated_halves(pid):
        """Check if the number has two identical halves."""
        s = str(pid)
        mid = len(s) // 2
        return s[:mid] == s[mid:]

    @staticmethod
    def has_any_repeated_split(pid):
        """Check if the number can be split into N identical parts."""
        s = str(pid)
        for n_parts in range(2, len(s)+1):
            if len(s) % n_parts != 0:
                continue
            splits = ProductIDProcessor.split_in_n(s, n_parts)
            if all(x == splits[0] for x in splits):
                return True
        return False

    def sum_repeated_halves(self):
        """Compute sum of IDs where two halves are identical."""
        total = 0
        for low, high in self.ranges:
            for pid in range(low, high+1):
                if self.has_repeated_halves(pid):
                    print(f"Repeated ID (halves): {pid}")
                    total += pid
        return total

    def sum_any_repeated_split(self):
        """Compute sum of IDs where any equal split exists."""
        total = 0
        for low, high in self.ranges:
            for pid in range(low, high+1):
                if self.has_any_repeated_split(pid):
                    total += pid
        return total


# ---------------------------
# Usage
processor = ProductIDProcessor("data/day2.txt")

# Part 1
total_halves = processor.sum_repeated_halves()
print(f"Total of repeated halves: {total_halves}")

# Part 2
total_any_split = processor.sum_any_repeated_split()
print(f"Total of any repeated IDs: {total_any_split}")