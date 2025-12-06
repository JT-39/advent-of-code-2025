with open("data/day1.txt", "r") as file:
    safe_codes = file.read().splitlines()

clean_codes_left = [code.replace("L", "-") for code in safe_codes]
clean_codes = [int(code.replace("R", "")) for code in clean_codes_left]

start_no = 50
number_past_0 = 0
for i in clean_codes:
    start_no += i
    if start_no == 0 or start_no == 100:
        number_past_0 += 1
    if start_no > 99:
        start_no - 100
    if start_no < 0:
        start_no + 100
    print(start_no)

print(number_past_0)


