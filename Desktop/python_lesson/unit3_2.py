def divide_numbers():
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    
    # Check for division by zero
    if denominator == 0:
        print("Error: Please enter a valid denominator.")
        divide_numbers()
    else:
        result = numerator / denominator
        print(f"The result is: {result}")

divide_numbers()

