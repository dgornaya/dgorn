#!/usr/bin/python3
import random
options = ['A', 'T', 'G', 'C']
lengh = 150
sequence = [random.choice(options) for _ in range(lengh)]
print(''.join(sequence))

counts = {}
for base in sequence:
    counts[base] = counts.get(base,0) +1

for base, count in counts.items():
    print(f"{base}: {count}")


