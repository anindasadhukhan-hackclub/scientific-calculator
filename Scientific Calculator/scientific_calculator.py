import math
import statistics

# Arithmetic
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y

def divide(x, y):
    return "Error: Division by zero" if y == 0 else x / y

def percentage(x, y):
    return "Error: Division by zero" if y == 0 else (x / y) * 100

# Trigonometry
def sin_val(x): return math.sin(x)
def cos_val(x): return math.cos(x)
def tan_val(x): return math.tan(x)

# Other
def sqrt_val(x): return math.sqrt(x)
def power(x, y): return math.pow(x, y)
def log_val(x, base): return math.log(x, base)

# Statistics
def mean(nums): return statistics.mean(nums)
def median(nums): return statistics.median(nums)
def mode(nums): return statistics.mode(nums)
def maximum(nums): return max(nums)
def minimum(nums): return min(nums)
