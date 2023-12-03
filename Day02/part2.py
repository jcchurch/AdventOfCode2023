import sys

total = 0
for line in open(sys.argv[1]):
    (game, pulls) = line.strip().split(": ")
    id = int(game[5:])

    balls = {}
    for pull in pulls.split("; "):
        for pairs in pull.split(", "):
            (count, color) = pairs.split(" ")
            count = int(count)

            if color in balls:
                if balls[color] < count:
                    balls[color] = count
            else:
                balls[color] = count

    total += balls["red"] * balls["green"] * balls["blue"]

print(total)
