import sys

total = 0
for line in open(sys.argv[1]):
    nums = []
    for ch in line:
        if ch in "0123456789":
            nums.append(int(ch))

    total += nums[0] * 10 + nums[-1]
print(total)
