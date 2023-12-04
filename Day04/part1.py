import sys
import re

def score_card(line):
    (card, numbers) = re.split(r': +', line.strip())
    (winning, mine) = re.split(r' \| ', numbers.strip())
    winning = sorted([int(x) for x in re.split(r' +', winning.strip())])
    mine = sorted([int(x) for x in re.split(r' +', mine.strip())])

    match_count = 0
    w = 0
    m = 0
    while m < len(mine) and w < len(winning):
        if mine[m] == winning[w]:
            match_count += 1
            w += 1
            m += 1
        elif winning[w] < mine[m]:
            w += 1
        else:
            m += 1
    if match_count == 0:
        return 0
    return 2 ** (match_count - 1)

score = 0
for line in open(sys.argv[1]):
    score += score_card(line)
print(score)
