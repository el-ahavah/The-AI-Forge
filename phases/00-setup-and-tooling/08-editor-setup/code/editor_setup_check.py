"""Temporary checks for the Lesson 8 VS Code setup."""


def greet(name: str) -> str:
    return f"Hello, {name}"


message = greet("Ahavah")
print(message)

# Intentional type mismatch: Pylance should flag the integer argument.
greet(25)


# Deliberately unformatted: Black should reformat this when the file is saved.
def calculate_total(price,quantity):
    total=price*quantity
    return total
