def calculate_area_rectangle(length: float, width: float) -> float:
    area = length * width
    return area

def main():
    try:
        # Example usage of calculate_area_rectangle function
        print("Area of rectangle:", calculate_area_rectangle(5.0, 3.0))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
