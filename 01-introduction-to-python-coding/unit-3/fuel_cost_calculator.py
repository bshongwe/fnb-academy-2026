# South African Fuel Cost Calculator Challenge

def display_row(label, value):
    """Helper function to print a formatted table row."""
    print(f"{label:<30} {value}")

def run_fuel_calculator():
    print("\n" + "=" * 45)
    print(f"{'SA FUEL COST CALCULATOR':^45}")
    print("=" * 45)

    # 1. Ask the user for kilometers to drive (type casting to float)
    kilometers = float(input("Enter kilometers to drive: "))

    # 2. Ask the user for the current petrol price per liter
    petrol_price = float(input("Enter current petrol price per liter (R): "))

    # 3. Calculate liters needed (1 liter per 10 km)
    liters_needed = round(kilometers / 10, 2)

    # 4. Calculate total cost
    total_cost = round(liters_needed * petrol_price, 2)

    # 5. Display results in a formatted table
    print("\n" + "-" * 45)
    print(f"{'TRIP SUMMARY':^45}")
    print("-" * 45)
    display_row("Distance:", f"{kilometers} km")
    display_row("Fuel Consumption:", f"1L per 10km")
    display_row("Petrol Price:", f"R{petrol_price} per liter")
    print("-" * 45)
    display_row("Liters Needed:", f"{liters_needed}L")
    display_row("Total Fuel Cost:", f"R{total_cost}")
    print("=" * 45)

# Run the calculator
run_fuel_calculator()