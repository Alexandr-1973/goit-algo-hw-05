import re
from typing import Callable

def generator_numbers(text: str):
    while text:
        text_part_match=re.search(r"\D*?\s\d+(\.\d+)?",text)
        if text_part_match:
            text_part=text_part_match.group()
            yield float(text_part.split(" ")[-1])
            text = text[text_part_match.end():]
        else:
            break

def sum_profit(text: str, func: Callable):
    return sum(list(func(text)))

text = ("Загальний дохід працівника складається з декількох"
        " частин: 1000.01 як основний дохід, доповнений додатковими"
        " надходженнями 27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


