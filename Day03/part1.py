import sys

digits_string = "0123456789"
all_numbers = []
just_this_symbol = set()

def get_number_if_digit(lines, i, j):
    if i >= 0 and j >= 0 and i < len(lines) and j < len(lines[0]) and lines[i][j] in digits_string:
        p = j
        q = j
        while p >= 1 and lines[i][p-1] in digits_string:
            p -= 1
        while q+1 < len(lines[0]) and lines[i][q+1] in digits_string:
            q += 1
        just_this_symbol.add( int(lines[i][p:q+1]) )

def get_all_numbers(lines, i, j):
    just_this_symbol.clear()
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            get_number_if_digit(lines, x, y)

    for number in just_this_symbol:
        all_numbers.append(number)

lines = []
for line in open(sys.argv[1]):
    lines.append(line.strip())

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] not in "0123456789.":
            get_all_numbers(lines, i, j)

total = 0
for number in all_numbers:
    total += number
print(total)
