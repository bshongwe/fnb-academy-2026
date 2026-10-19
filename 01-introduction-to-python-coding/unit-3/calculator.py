# calculator.py - Optimized Multi-Function Calculator

DIVISION_BY_ZERO_ERROR = "Cannot divide by zero!"

def display_row(label, value):
    """Helper function to print a formatted table row."""
    print(f"{label:<25} {value}")

def run_calculator():
    # Collect user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Store basic operations in a dictionary
    results = {
        "Addition":       round(num1 + num2, 2),
        "Subtraction":    round(num1 - num2, 2),
        "Multiplication": round(num1 * num2, 2),
    }

    # Handle division operations
    division_ops = {}
    if num2 == 0:
        division_ops = {
            "Division":          DIVISION_BY_ZERO_ERROR,
            "Floor Division (//)" : DIVISION_BY_ZERO_ERROR,
            "Modulus (%)":       DIVISION_BY_ZERO_ERROR,
        }
    else:
        division_ops = {
            "Division":           round(num1 / num2, 2),
            "Floor Division (//)" : round(num1 // num2, 2),
            "Modulus (%)":        round(num1 % num2, 2),
        }

    # Merge all results
    results.update(division_ops)

    # Display formatted table
    print("\n" + "=" * 40)
    print(f"{'MULTI-FUNCTION CALCULATOR':^40}")
    print("=" * 40)
    display_row("Number 1:", num1)
    display_row("Number 2:", num2)
    print("-" * 40)

    for label, value in results.items():
        display_row(f"{label}:", value)

    print("=" * 40)

# Run the calculator
run_calculator()