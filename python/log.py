from math import log

y = [log(x) for x in range(1, 11)]

# Correct and idiomatic Python:
y2 = map(log, range(1, 11))

# Will this produce a different answer?
map(lambda x: log(x), range(1, 11))

# Does this work?
map(log(x), range(1, 11))

