# naming_violation.py - naming violation for agentic reviewer

def CalculateSum(arr: list[int]) -> int:
    totalSum = 0
    for i in arr:
        totalSum += i
    return totalSum

def GreetUser(Name: str) -> None:
    print("Hello, " + Name)

class BAD_CLASSNAME:
    def __init__(self, data):
        self.dataVal = data

def getresult(x, y): # should be get_result
    return x + y

def computeSumandProduct(a, b): # should be compute_sum_and_product
    sumVal = a + b
    prodVal = a * b
    return sumVal, prodVal

MagicNumber = 42
