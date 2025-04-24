import numpy as np
import pandas as pd
from scipy.stats import norm

# Generate random data for demonstration
np.random.seed(0)
data = np.random.randn(10)

def compute_quantile(data, quantiles):
    """
    Compute quantiles using the Quantile function from Scipy.

    Args:
        data (numpy.ndarray): Data points.
        quantiles: List of quantiles to compute.

    Returns:
        numpy.ndarray: Array containing the computed quantiles.
    """
    return norm.qstats(data, quantiles)

# Example usage
quantiles = [0.25, 0.5, 0.75]
result = compute_quantile(data, quantiles)
print(result)
