# Part 1
# Open safe codes in a list
with open("data/day1.txt", "r") as file:
    safe_codes = file.read().splitlines()

test=["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82", "R150", "L180", "R2"]

# Left turns are -ve, right +ve
codes_num = [int(code.replace("L", "-").replace("R", "")) for code in safe_codes]

# Parameters
start_num = 50
safe_pointer = start_num
number_land_0 = 0

# safe_pointer is where the safe is turned to,
# if divisible by 100 or equal to 0 we know lands on 0
for i in codes_num:
    # Where the safe is pointing after the turn
    safe_pointer = (safe_pointer + i) % 100
    if (safe_pointer % 100 == 0) or (safe_pointer == 0):
        number_land_0 += 1

# Part 1 answer
print(f'Number of times safe lands on zero: {number_land_0}')


# Part 2
# Parameters
start_num = 50
safe_pointer = start_num
number_pass_0 = 0

# Find where the safe pointer passes 0 (or 100)
for i in codes_num:
    # Calculate safe pointer total
    safe_pointer_total = safe_pointer + i

    # Passes 100 (for right turns), add a count
    if (safe_pointer_total >= 100):
        number_pass_0 += 1
    # Passes 0 (for left turns) and was not previously 0, add a count
    if (safe_pointer_total <= 0 and safe_pointer!=0):
        number_pass_0 += 1
    
    # Where the safe is pointing after the turn 
    safe_pointer = safe_pointer_total % 100
    
    # For turns greater than 100
    # For right turns add a count for each 100 turns (minus a count for the already added count for passing 100)
    # E.g., safe_pointer = 20, turn = R130, pointer passes 100 once and ends up pointing to 50 (the first pass is counted above)
    if i > 100:
        num_clicks = (abs(safe_pointer_total)// 100) -1
        number_pass_0 += num_clicks
    
    # For left turns add a count for each 100 turns (no minus count as over -100 turn will always pass 0 twice)
    # E.g., safe_pointer = 20, turn = -R130, pointer passes 0 once after -20 turns, then again after -100 turns and ends up pointing to 90 (-10 turns after that)
    if i < -100:
        num_clicks = (abs(safe_pointer_total)// 100)
        number_pass_0 += num_clicks
    

# Part 2 answer
print(f'Number of times safe passes on zero: {number_pass_0}')


