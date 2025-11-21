# Manually define functions to perform statistical stuff
# Note: Can't name a python file "statistics.py" because it interferes with python objects called "statistics".
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def get_standard_deviation(sample: list):
    import math

    mean = sum(sample) / len(sample)                    # Average value in sample.
    deviations = [mean - n for n in sample]             # How much each value is different from the mean average.
    squared_deviations = [d * d for d in deviations]    # Square the deviations to remove nevative values.
    variance = sum(squared_deviations) / len(sample)    # Get the average of the squared deviations.
    return math.sqrt(variance)                          # Square root to get the deviation in the original "un-squared" scale.

def one_sample_t_test(sample: list, hypothosis_mean):
    import math

    mean = sum(sample) / len(sample)
    standard_deviation = get_standard_deviation(sample)
    logger.info(f"Standard deviation is: {standard_deviation}")
    sample_size = len(sample)

    return (mean - hypothosis_mean) / (standard_deviation / math.sqrt(sample_size))

def p_value(sample: list, hypothosis_mean):
    from scipy import stats

    t_value = one_sample_t_test(sample, hypothosis_mean)

    degrees_of_freedom = len(sample) - 1    # Number of "steps" between all the sample values.
    logger.info(f"Degrees of freedom (df) is: {degrees_of_freedom}")

    logger.info(f"The t-value is: {t_value}")
    logger.info(f"In a t-distribution table, look at the line where the degrees of freedom (df) is {degrees_of_freedom} and identify which columns (p-levels) the t-value {t_value:.3f} is between.")
    logger.info("Example t-distribution table: https://www.stat.purdue.edu/~lfindsen/stat503/t-Dist.pdf")
    logger.info(f"Being a one-sample t-test, getting the average of these p-levels will give you the p-value. (If it was a two-sample test, multiply this by 2 to get the p-value)")