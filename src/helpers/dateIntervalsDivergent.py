from classes.Date import Date


def dateIntervalsDivergent(aStart: Date, aEnd: Date, bStart: Date, bEnd: Date):
    # czy dwa przedziały czasowe (a oraz b) są rozłączne
    # mogą mieć tylko jeden wspólny dzień
    return aEnd <= bStart or aStart >= bEnd
