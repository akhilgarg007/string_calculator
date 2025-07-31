def add(numbers: str) -> int:
    if not numbers:
        return 0
    parts = numbers.split(",")
    return sum(map(int, parts))
