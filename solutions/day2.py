with open("data/day2.txt", "r") as file:
    product_id_ranges = file.read().split(",")
    product_id_ranges = [p.rstrip() for p in product_id_ranges]


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