import numpy as np

# Define function
def calculate_area(shape):
    if shape == "square":
        return 4 * 2
    elif shape == "rectangle":
        return 2 * (shape[0] + shape[1])
    elif shape == "circle":
        return np.pi * shape[0] ** 2
    else:
        raise ValueError("Unsupported shape: {}".format(shape))

# Example usage
shape = "square"
area = calculate_area(shape)
print(f"The area of a {shape} is {area}")
