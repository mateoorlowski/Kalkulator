from math import sqrt as math_sqrt, sin as math_sin, cos as math_cos, tan as math_tan, factorial, log, pi, radians, log10 as math_log10

def add(x: float, y: float) -> float:
    return x + y

def subtract(x: float, y: float) -> float:
    return x - y

def multiply(x: float, y: float) -> float:
    return x * y

def divide(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def pow(x: float, y: float) -> float:
    return x ** y

def sqrt(x: float) -> float:
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math_sqrt(x)

def sin(x: float) -> float:
    return math_sin(radians(x))

def cos(x: float) -> float:
    return math_cos(radians(x))

def tan(x: float) -> float:
    return math_tan(radians(x))

def cot(x: float) -> float:
    return 1 / math_tan(radians(x))

def fac(x: int) -> int:
    if x < 0:
        raise ValueError("Cannot calculate factorial of a negative number")
    return factorial(x)

def ln(x: float) -> float:
    if x <= 0:
        raise ValueError("Cannot calculate natural logarithm of a non-positive number")
    return log(x)

def log_base(x: float, base: float) -> float:
    if x <= 0 or base <= 0 or base == 1:
        raise ValueError("Invalid input for logarithm calculation")
    return log(x, base)

def circ(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return pi * (radius ** 2)

def rect(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")
    return length * width

def lin(a: float, b: float) -> float:
    if a == 0:
        raise ValueError("The coefficient 'a' in a linear equation cannot be zero")
    return -b / a

def quad(a: float, b: float, c: float) -> tuple[float, float]:
    if a == 0:
        raise ValueError("The coefficient 'a' in a quadratic equation cannot be zero")

    delta = b**2 - 4*a*c

    if delta < 0:
        raise ValueError("The equation has no real roots")
    elif delta == 0:
        x = -b / (2*a)
        return x, x

    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)

    return x1, x2

def absolute(x: float) -> float:
    return abs(x)

def mod(x: float, y: float) -> float:
    return x % y

def log10(x: float) -> float:
    if x <= 0:
        raise ValueError("Cannot calculate logarithm of a non-positive number")
    return math_log10(x)

def dec_to_bin(decimal: int) -> str:
    if decimal < 0:
        return '-' + bin(abs(decimal))[2:]
    else:
        return bin(decimal)[2:]

def dec_to_oct(decimal: int) -> str:
    if decimal < 0:
        return '-' + oct(abs(decimal))[2:]
    else:
        return oct(decimal)[2:]

def dec_to_hex(decimal: int) -> str:
    if decimal < 0:
        return '-' + hex(abs(decimal))[2:]
    else:
        return hex(decimal)[2:]
