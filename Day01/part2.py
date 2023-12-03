import sys

total = 0
for line in open(sys.argv[1]):
    nums = []
    i = 0
    for ch in line:
        if line.startswith("zero", i): nums.append(0)
        if line.startswith("one", i): nums.append(1)
        if line.startswith("two", i): nums.append(2)
        if line.startswith("three", i): nums.append(3)
        if line.startswith("four", i): nums.append(4)
        if line.startswith("five", i): nums.append(5)
        if line.startswith("six", i): nums.append(6)
        if line.startswith("seven", i): nums.append(7)
        if line.startswith("eight", i): nums.append(8)
        if line.startswith("nine", i): nums.append(9)
        if ch in "0123456789":
            nums.append(int(ch))
        i += 1

    total += nums[0] * 10 + nums[-1]
print(total)
