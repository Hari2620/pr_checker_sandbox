# naming_violation.py

def CalculateSum(arr: list[int]) -> int:
    totalSum = 0
    for i in arr:
        totalSum += i
    return totalSum

def GreetUser(Name: str) -> None:
    print("Hello, " + Name)
