# Tyler Camphouse 
# UWYO COSC 1010
# Submission Date 11/04/24
# Lab 08
# Lab Section: 16
# Sources, people worked with, help given to:
# Python Crash Course, 3rd Edition
# Repit AI helper

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def convert_to_number(string):
  """
  Checks if a string can be converted to an integer or float and returns the converted value.
  Args:
      string: The string to be converted.
  Returns:
      int or float: The converted integer or float, or False if the string cannot be converted.
  """
  negative = False
  if string[0] == "-":
    negative = True
    string = string.replace("-","")
  if "." in string:
    number = string.replace(".")
    if len(number) == 2 and number[0].isdigit() and number[1].isdigit():
      if negative:
        return -1*float(string)
      else:
        return float(string)
    else:
      return False
  elif string.isdigit():
    if negative:
      return -1*int(string)
    else:
      return int(string)
  return False
print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def slope_intercept(m, b, lower_bound, upper_bound):
  """
  Calculates the y-values for a given slope, intercept, and x-range.
  Args:
      m: The slope of the line (float or int).
      b: The y-intercept (float or int).
      lower_bound: The lower x-bound (int).
      upper_bound: The upper x-bound (int).
  Returns:
      list: A list of y-values for the given x-range, or False if the input is invalid.
  """
  if lower_bound >= upper_bound or not isinstance(lower_bound, int) or not isinstance(upper_bound, int):
    return False
  y_values = []
  for x in range(lower_bound, upper_bound + 1):
    y = m * x + b
    y_values.append(y)
  return y_values
while True:
  m_input = input("Enter the slope (m): ")
  if m_input == "exit":
    break
  b_input = input("Enter the y-intercept (b): ")
  if b_input == "exit":
    break
  lower_bound_input = input("Enter the lower x-bound: ")
  if lower_bound_input == "exit":
    break
  upper_bound_input = input("Enter the upper x-bound: ")
  if upper_bound_input == "exit":
    break
  try:
    m = convert_to_number(m_input)
    b = convert_to_number(b_input)
    lower_bound = convert_to_number(lower_bound_input)
    upper_bound = convert_to_number(upper_bound_input)
    result = slope_intercept(m, b, lower_bound, upper_bound)
    if result:
      print(f"Y-values: {result}")
    else:
      print("Invalid input: Lower bound must be less than or equal to the upper bound, and both must be integers.")
  except ValueError:
    print("Invalid input: Please enter valid numbers.")
print("*" * 75)

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
import cmath
def quadratic_solver(a, b, c):
  """
  Solves a quadratic equation using the quadratic formula.
  Args:
      a: The coefficient of the x^2 term (float).
      b: The coefficient of the x term (float).
      c: The constant term (float).
  Returns:
      tuple: A tuple containing the two possible solutions (complex numbers or floats).
  """
  delta = (b**2) - 4 * (a * c)
  if delta >= 0:
    x1 = (-b - delta**0.5) / (2 * a)
    x2 = (-b + delta**0.5) / (2 * a)
    return (x1, x2)
  else:
    x1 = (-b - cmath.sqrt(delta)) / (2 * a)
    x2 = (-b + cmath.sqrt(delta)) / (2 * a)
    return (x1, x2)
while True:
  a_input = input("Enter the coefficient of x^2 (a): ")
  if a_input == "exit":
    break
  b_input = input("Enter the coefficient of x (b): ")
  if b_input == "exit":
    break
  c_input = input("Enter the constant term (c): ")
  if c_input == "exit":
    break
  try:
    a = convert_to_number(a_input)
    b = convert_to_number(b_input)
    c = convert_to_number(c_input)
    solution = quadratic_solver(a, b, c)
    print(f"Solutions: {solution}")
  except ValueError:
    print("Invalid input: Please enter valid numbers.")