with open("data/day2.txt", "r") as file:
    product_id_ranges = file.read().split(",")
    product_id_ranges = [p.rstrip() for p in product_id_ranges]

# Part 1
product_id_ranges = [range.split("-") for range in product_id_ranges]
product_id_ranges = [[int(p) for p in range] for range in product_id_ranges]

# Count of repeated IDs
num_rep_ids = 0

# Loop over each ID in the range
for p_id_range in product_id_ranges:
    for p_id in range(p_id_range[0], p_id_range[1]+1):
        # Split ID in 1/2
        p_id_chr = str(p_id)
        firstpart, secondpart = p_id_chr[:len(p_id_chr)//2], p_id_chr[len(p_id_chr)//2:]

        # If the halves match, add ID value to the count
        if firstpart == secondpart:
            num_rep_ids += p_id
            print(f"Repeated ID: {firstpart}, {secondpart}")


# Part 1 answer
print(f"Total of repeated IDs: {num_rep_ids}")

# Part 2
# Split words by n
def split_in_n(word, n):
    length = len(word)
    part_len = length // n

    return [word[i*part_len:(i+1)*part_len] for i in range(n)]

# Count of repeated IDs
num_any_rep_ids = 0

for p_id_range in product_id_ranges:
    for p_id in range(p_id_range[0], p_id_range[1]+1):
        
        p_id_chr = str(p_id)
        # Loop other each num in the id length and try splitting the id by that num
        for letter in range(2, len(p_id_chr)+1):
            # Skip nums that don't divide the length into a whole number 
            if len(p_id_chr) % letter != 0:
                continue
            splits = split_in_n(p_id_chr, letter)
        
            # Count ids where the splits are all equal
            if splits.count(splits[0]) == len(splits):
                num_any_rep_ids += p_id
                break

# Part 2 answer
print(f"Total of any repeated IDs: {num_any_rep_ids}")


