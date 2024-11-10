import re
from typing import Callable

def generator_numbers(text: str):
    while text:
        number_text_match=re.search(r" \d+?(\.\d+)? ", text)
        if number_text_match:
            yield float(number_text_match.group().strip())
            text = text[number_text_match.end():]
        else:
            break

def sum_profit(text: str, func: Callable):
    return sum(list(func(text)))

text = ("Загальний дохід працівника складається з декількох"
        " частин: 1000.01 як основний дохід, доповнений додатковими"
        " надходженнями 27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


