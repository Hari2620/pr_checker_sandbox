# good_code.py - good code for agentic reviewer

def calculate_sum(numbers: list[int]) -> int:
    """Return the sum of a list of integers."""
    return sum(numbers)

def greet_user(username: str) -> None:
    """Print a greeting message."""
    print(f"Hello, {username}!")

def square(x: int) -> int:
    """Return square of x."""
    return x * x

def average(nums: list[float]) -> float:
    """Return average of a list of numbers."""
    if not nums:
        return 0.0
    return sum(nums) / len(nums)
