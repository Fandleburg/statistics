# Manually define functions to perform statistical stuff
# Note: Can't name a python file "statistics.py" because it interferes with python objects called "statistics".

def standard_deviation(sample):
    import math

    mean = sum(sample) / len(sample)
    deviations = [mean - n for n in sample]
    squared_deviations = [d * d for d in deviations]
    variance = sum(squared_deviations) / len(sample)
    return math.sqrt(variance)