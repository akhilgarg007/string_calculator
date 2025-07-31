import re


def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiters = [",", "\n"]

    if numbers.startswith("//"):
        header, numbers = numbers.split('\n', 1)
        custom_delim = header[2:]
        delimiters.append(re.escape(custom_delim))

    pattern = "|".join(delimiters)
    parts = re.split(pattern, numbers)

    negatives = []
    total = 0
    for part in parts:
        num = int(part)
        if num < 0:
            negatives.append(num)
        elif num <= 1000:
            total += num

    if negatives:
        raise Exception(f"negatives not allowed: {', '.join(map(str, negatives))}")

    return total