# complexity_violation.py - complexity violation
from typing import Optional

def process_data(data: list[int]) -> list[Optional[int]]:
    result: list[Optional[int]] = []
    for value in data:
        if value > 0:
            if value % 2 == 0:
                result.append(value * 2)
            else:
                for _ in range(value):
                    result.append(value)
        elif value < 0:
            if abs(value) > 10:
                result = [abs(v) for v in data if v < 0]
            else:
                result.append(0)
        else:
            result.append(None)
    return result

def deeply_nested(a: int, b: int) -> int:
    # Deeply nested conditionals
    if a > 0:
        if b > 0:
            if a % 2 == 0:
                if b % 2 == 0:
                    return a + b
                else:
                    return a - b
            else:
                if b % 2 == 0:
                    return b - a
                else:
                    return a * b
        else:
            if a > 100:
                return a // 2
            else:
                return 0
    else:
        return -1

def long_function():
    # Excessively long function for cyclomatic complexity
    s = 0
    for i in range(10):
        if i % 2 == 0:
            s += i
        if i % 3 == 0:
            s -= i
        if i % 5 == 0:
            s += i * 2
        if i % 7 == 0:
            s -= i // 2
    for j in range(10):
        s += j
        for k in range(3):
            s -= k
    return s

# Duplicate code
def duplicate_logic(x):
    if x > 10:
        return x * 2
    else:
        return x + 2

def duplicate_logic2(y):
    if y > 10:
        return y * 2
    else:
        return y + 2
