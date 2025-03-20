# Errors

Q1.

```Python
def calculate_area(radius):
    area = 3.14 x radius x 2
    return area

print(calculate_area(5))
print(calculate_area(3))
```

A: It is a syntax error, "x" is not how you mutliple numbers together in Python, hence the program will be incapable of understanding the operation and a syntax error will be returned.

```Python
import math
def calculate_area(radius):
    area = math.pi * radius ** 2
    return area

print(calculate_area(5))
print(calculate_area(3))
```

Q2.

```Python
def calculate_area(length, width):
    return length + width

area = calculate_area(5, 3)
print(f"Area: {area}")
```

A: This is a logic error, it uses an incorrect formula to calculate the area of a rectangle. The correct formula is length x width (l x w), hence due to the incorrect formula the program suffers from a logic error hence returning an incorrect answer.

```Python
def calculate_area(length, width):
    return length * width

area = calculate_area(5, 3)
print(f"Area: {area}")
```

Q3.

```Python
def divide(a, b):
    return a / b

result = divide(10, 0)
print(result)
```

A: This is a runtime error, due to division by 0 being undefined it will not be capable of giving a response and just crash.

```Python
def divide(a, b):
   try:
     return a / b
   except ZeroDivisonError:
     return "Cannot divide by zero."

result = divide(10, 0)
print(result)
```

Q4.

```Python
for i in range(5)
    print(i)
```

A: This is a syntax error, it lacks a crucial ":"  to allow the "for" function to run as intended, hence the program suffers from a syntax error due to the careless mistake of forgetting the ":" required for functions that require indents.

```Python
for i in range(5):
    print(i)
```

Q5.

```Python
def calculate_average(numbers):
    total = sum(numbers)
    return total - len(numbers)

numbers = [10, 20, 30, 40]
average = calculate_average(numbers)
print(f"Average: {average}")
```

A: This is a logic error, it minuses the amount of numbers instead of dividing the total by it. Hence the program incorrectly calculates the average due to using the wrong operation, hence creating a logic error.

```Python
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

numbers = [10, 20, 30, 40]
average = calculate_average(numbers)
print(f"Average: {average}")
```

Q6.

```Python
def calculate_area(diameter):
    return math.pi * diameter ** 2

print(calculate_area(5))
```

A: There is actually a name error due to the math import having not been... imported, hence "math.pi" is undefined causing a name error, but assuming it does secretly have math imported then it still suffers from a logic error as it uses diameter instead of radius for the calculation. Hence it immediately suffers from a name error due to math.pi being undefined but if it were imported it'd suffer a logic error from using the diameter instead of radius.

```Python
import math

def calculate_area(diameter):
    return math.pi * (diameter/2) ** 2

print(calculate_area(5))
```
