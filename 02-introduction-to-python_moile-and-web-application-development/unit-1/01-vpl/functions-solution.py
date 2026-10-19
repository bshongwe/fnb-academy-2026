# =====================================================================
#  PRACTICAL: DEFINING AND USING FUNCTIONS
# =====================================================================
#  Complete every function marked with a TODO.
#
#  RULES:
#   1. Do NOT change the function names or their parameters.
#   2. Do NOT change any code below the "DO NOT MODIFY" line.
#   3. Your functions must RETURN values, not print them.
#      The main() function does all the printing for you.
# =====================================================================


def greet(name):
    """
    Return a greeting of the form:  Hello, <name>!

    Example:
        greet("Thabo")  ->  "Hello, Thabo!"
    """
    return f"Hello, {name}!"


def rectangle_area(length, width):
    """
    Return the area of a rectangle.

    Both dimensions must be non-negative.

    Example:
        rectangle_area(5, 4)  ->  20.0
    """
    if length < 0 or width < 0:
        raise ValueError("Rectangle dimensions cannot be negative.")
    return length * width


def is_even(number):
    """
    Return True if number is even, and False if it is odd.

    Hint: the modulus operator (%) gives you the remainder.

    Example:
        is_even(12)  ->  True
        is_even(7)   ->  False
    """
    return number % 2 == 0


def count_vowels(text):
    """
    Return how many vowels (a, e, i, o, u) appear in text.
    Upper case and lower case vowels both count.

    Example:
        count_vowels("Programming is fun")  ->  5
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def factorial(n):
    """
    Return n factorial (n!), i.e. n * (n-1) * (n-2) * ... * 1
    By definition, factorial(0) is 1.
    n must be non-negative.

    Example:
        factorial(5)  ->  120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def apply_discount(price, percentage=10):
    """
    Return the price after subtracting the given percentage.
    'percentage' is a DEFAULT PARAMETER: when the caller leaves it out,
    a 10% discount must be applied.
    The price must be non-negative, and percentage must be between 0 and 100.
    Round the answer to 2 decimal places.

    Example:
        apply_discount(200)      ->  180.0
        apply_discount(250, 20)  ->  200.0
    """
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if percentage < 0 or percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    discounted_price = price - (price * percentage / 100)
    return round(discounted_price, 2)


# =====================================================================
#  DO NOT MODIFY ANYTHING BELOW THIS LINE
# =====================================================================
def main():
    command = input().strip().lower()

    if command == "greet":
        print(greet(input().strip()))
    elif command == "area":
        print(rectangle_area(float(input()), float(input())))
    elif command == "even":
        print(is_even(int(input())))
    elif command == "vowels":
        print(count_vowels(input()))
    elif command == "factorial":
        print(factorial(int(input())))
    elif command == "discount":
        print(apply_discount(float(input())))
    elif command == "discount_custom":
        print(apply_discount(float(input()), float(input())))
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()