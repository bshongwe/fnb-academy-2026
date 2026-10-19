# =====================================================================
#  PRACTICAL: FUNCTIONS 2 - RETURNING, COMPOSING AND RECURSING
# =====================================================================

def evens_up_to(n):
    """
    Return a LIST of every even number from 0 up to and including n.
    """
    result = []
    for i in range(0, n + 1):
        if i % 2 == 0:
            result.append(i)
    return result

def min_max(numbers):
    """
    Return TWO values - the smallest and the largest number in the list,
    in that order.
    """
    return min(numbers), max(numbers)

def safe_divide(a, b):
    """
    Return a divided by b.
    If b is zero, return None instead of crashing.
    """
    if b == 0:
        return None
    return a / b

def total(numbers):
    """
    Return the sum of all the numbers in the list.
    """
    sum_so_far = 0
    for number in numbers:
        sum_so_far += number
    return sum_so_far

def average(numbers):
    """
    Return the average of the numbers in the list.
    You MUST call total() to work out the sum.
    If the list is empty, return None.
    """
    if len(numbers) == 0:
        return None
    return total(numbers) / len(numbers)

def initials(full_name):
    """
    Return the initials of a name, in upper case, separated by full stops.
    """
    words = full_name.split()
    letters = [word[0].upper() for word in words]
    return ".".join(letters) + "."

def format_currency(amount, symbol="R"):
    """
    Return the amount as a currency string with exactly two decimal places.
    """
    return f"{symbol}{amount:.2f}"

def countdown(n):
    """
    Return a countdown string from n down to 1, followed by Liftoff.
    Must use recursion.
    """
    if n <= 0:
        return "Liftoff"
    return str(n) + " " + countdown(n - 1)

def print_table(n):
    """
    PRINT the times table for n, from 1 to 10, one line per row.
    """
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