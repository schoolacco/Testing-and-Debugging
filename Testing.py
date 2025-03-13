def is_safe_temperature(temp):
    return 0 <= temp <= 100

# TODO: Write test cases for boundary values
print("Testing lower bound")
print(is_safe_temperature(0))
print(is_safe_temperature(1))
print(is_safe_temperature(-1))
print("\nTesting upper bound")
print(is_safe_temperature(100))
print(is_safe_temperature(99))
print(is_safe_temperature(101))
