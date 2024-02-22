def handle_zero_division(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except ZeroDivisionError:
            print("Error: Division by zero!")
            result = None  # You can choose a different default value or behavior here
        return result

    return wrapper

@handle_zero_division
def divide(a, b):
    return a / b

# Example usage
result1 = divide(10, 2)  # No error, result1 is 5.0
result2 = divide(5, 0)   # Error handled by decorator, result2 is None

print("Result 1:", result1)
print("Result 2:", result2)
