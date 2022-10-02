"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        mid = len(numbers) // 2
        if len(numbers)%2 == 0:
            median = (numbers[mid] + numbers[mid-1]) / 2
        else :
            median = numbers[mid]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)
