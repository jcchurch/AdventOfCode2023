import sys
import re

"""
X + Y = Time
X * Y >= Distance

Find the smallest X that meets the criteria.
"""

lines = []
for line in open(sys.argv[1]):
    lines.append(line)

times_str = re.split(r"\s*:\s*", lines[0])[1]
times = [int(x) for x in re.split(r"\s+", times_str.strip())]

distances_str = re.split(r"\s*:\s*", lines[1])[1]
distances = [int(x) for x in re.split(r"\s+", distances_str.strip())]

product = 1
for i in range(len(times)):
  time = times[i]
  distance = distances[i]

  low = 0
  high = time
  while low <= high:
      X = low + (high - low) // 2
      Y = time - X

      if X * Y > distance and (X-1)*(Y+1) <= distance:
          break

      if X * Y <= distance:
          low = X + 1
      else:
          high = X - 1

  Y = time - X
  product *= Y + 1 - X

print(product)
