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
    return sum(map(int, parts))
