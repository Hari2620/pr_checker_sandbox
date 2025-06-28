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
