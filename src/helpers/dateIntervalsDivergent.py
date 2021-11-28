def dateIntervalsDivergent(aStart, aEnd, bStart, bEnd):
    return aEnd <= bStart or aStart >= bEnd
