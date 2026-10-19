# =====================================================================
#  PRACTICAL: FUNCTIONS 2 - RETURNING, COMPOSING AND RECURSING
# =====================================================================
#  Complete every function marked with a TODO.
#
#  RULES:
#   1. Do NOT change the function names or their parameters.
#   2. Do NOT change any code below the "DO NOT MODIFY" line.
#   3. Most of these functions must RETURN a value, not print it.
#      The one exception is print_table(), which is meant to print.
# =====================================================================


def evens_up_to(n):
    """
    Return a LIST of every even number from 0 up to and including n.

    Example:
        evens_up_to(8)  ->  [0, 2, 4, 6, 8]
        evens_up_to(5)  ->  [0, 2, 4]

    Note: you must return the list itself, not print the numbers.
    """
    # 1: build a list and return it
    return [i for i in range(0, n + 1, 2)]


def min_max(numbers):
    """
    Return TWO values - the smallest and the largest number in the list,
    in that order.

    Example:
        min_max([4, 9, 1, 7])  ->  1, 9

    Hint: a function can return more than one value by separating them
    with a comma.
    """
    # 2: use the built-in min() and max() functions
    return min(numbers), max(numbers)


def safe_divide(a, b):
    """
    Return a divided by b.
    If b is zero, return None instead of crashing.

    Example:
        safe_divide(10, 4)  ->  2.5
        safe_divide(10, 0)  ->  None

    Hint: check for the bad case first and return early.
    """
    # 3: check for b == 0, return None, otherwise return a / b
    if b == 0:
        return None
    return a / b


def total(numbers):
    """
    Return the sum of all the numbers in the list.
    An empty list has a total of 0.

    Example:
        total([2, 4, 6])  ->  12
    """
    # 4: use the built-in sum() function
    return sum(numbers)


def average(numbers):
    """
    Return the average of the numbers in the list.
    You MUST call total() to work out the sum - do not add them again here.
    If the list is empty, return None.

    Example:
        average([2, 4, 6])  ->  4.0
    """
    # 5: call total(numbers), then divide
    if not numbers:
        return None
    return total(numbers) / len(numbers)


def initials(full_name):
    """
    Return the initials of a name, in upper case, separated by full stops.

    Example:
        initials("temoso mokoena")   ->  "T.M."
        initials("Ada Grace Lovelace") -> "A.G.L."

    Hint: split the name into words, take the first letter of each.
    """
    # 6: split the name into words, take the first letter of each, join with "."
    words = full_name.split()
    return "".join([word[0].upper() + "." for word in words])


def format_currency(amount, symbol="R"):
    """
    Return the amount as a currency string with exactly two decimal places.
    'symbol' is a DEFAULT PARAMETER - when the caller leaves it out,
    use the Rand symbol.

    Example:
        format_currency(150)        ->  "R150.00"
        format_currency(9.5)        ->  "R9.50"
        format_currency(20, "$")    ->  "$20.00"
    """
    # 7: use an f-string to format the amount with two decimal places
    return f"{symbol}{amount:.2f}"


def countdown(n):
    """
    Return a countdown string from n down to 1, followed by Liftoff.
    Each part is separated by a single space.

    Example:
        countdown(5)  ->  "5 4 3 2 1 Liftoff"
        countdown(1)  ->  "1 Liftoff"
        countdown(0)  ->  "Liftoff"

    You MUST use recursion for this one - the function has to call
    itself. Think about:
        - the base case: when do you stop?
        - the recursive step: what smaller problem do you hand onwards?
    """
    # 8: use recursion to build the countdown string
    if n <= 0:
        return "Liftoff"
    return f"{n} {countdown(n - 1)}"


def print_table(n):
    """
    PRINT the times table for n, from 1 to 10, one line per row.
    This function PRINTS - it does not return anything.

    Example, print_table(3) prints:
        3 x 1 = 3
        3 x 2 = 6
        ...
        3 x 10 = 30
    """
    # 9: use a for loop to print the times table
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# =====================================================================
#  DO NOT MODIFY ANYTHING BELOW THIS LINE
# =====================================================================
def main():
    parts = input().strip().split()
    command = parts[0].lower()

    if command == "evens":
        print(evens_up_to(int(parts[1])))
    elif command == "minmax":
        low, high = min_max([int(p) for p in parts[1:]])
        print(low, high)
    elif command == "divide":
        print(safe_divide(float(parts[1]), float(parts[2])))
    elif command == "guard":
        print(safe_divide(10, 0), safe_divide(9, 3))
    elif command == "total":
        print(total([int(p) for p in parts[1:]]))
    elif command == "average":
        print(average([int(p) for p in parts[1:]]))
    elif command == "initials":
        print(initials(" ".join(parts[1:])))
    elif command == "money":
        print(format_currency(float(parts[1])))
    elif command == "money_symbol":
        print(format_currency(float(parts[1]), parts[2]))
    elif command == "countdown":
        print(countdown(int(parts[1])))
    elif command == "table":
        print_table(int(parts[1]))
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()