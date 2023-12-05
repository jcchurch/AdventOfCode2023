import sys
import re

maps = {}

lines = []
for line in open(sys.argv[1]):
    lines.append(line)

seeds = [int(x) for x in lines[0].split(": ")[1].split(" ")]

before = ""
after = ""
for line in lines[2:]:
    if "map" in line:
        (conversion, _) = line.split(" ")
        (before, after) = conversion.split("-to-")
        maps[before] = {
            "next": after,
            "records": []
        }
    elif line != "\n":
        (destination, source, spread) = [int(x) for x in line.split(" ")]
        maps[before]["records"].append({
            "source": source,
            "destination": destination,
            "spread": spread,
            "last": source + spread,
            "diff": destination - source
        })

all_scores = []
i = 0
while i < len(seeds):
    seed = seeds[i]
    count = seeds[i+1]

    for x in range(count):
        before = "seed"
        score = seed+x
        while before in maps:
            maps_to = score
            for record in maps[before]["records"]:
                if record["source"] <= score and score < record["last"]:
                    maps_to += record["diff"]
            before = maps[before]["next"]
            score = maps_to
        all_scores.append(score)
    i += 2

print(min(all_scores))
