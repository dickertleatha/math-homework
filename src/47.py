def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle.
        
    Returns:
        float: The area of the circle.
    """
    return 3.14 * radius ** 2

radius = 5
area = calculate_area(radius)
print("The area of the circle with radius", radius, "is:", area)
