def dateIntervalsDivergent(a, b):
    return a.end <= b.start or a.start >= b.end