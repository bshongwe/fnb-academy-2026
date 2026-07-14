# Advanced level - Student Info Formatter

def get_student_info() -> dict:
    """Collect and validate student information."""
    try:
        first_name = input("Enter your first name: ").strip().title()
        surname = input("Enter your surname: ").strip().title()
        age = int(input("Enter your age: ").strip())
        favourite_number = float(input("Enter your favourite number: ").strip())

        return {
            "first_name": first_name,
            "surname": surname,
            "age": age,
            "favourite_number": favourite_number
        }
    except ValueError as e:
        print(f"Invalid input: {e}. Please restart and try again.")
        exit(1)


def format_profile(info: dict) -> str:
    """Format student data into a profile card string."""
    full_name = f"{info['first_name']} {info['surname']}"
    age_in_months = info["age"] * 12
    rounded_favourite = round(info["favourite_number"], 2)

    return (
        f"\n{'=' * 40}\n"
        f"  Welcome, {full_name}!\n"
        f"{'=' * 40}\n"
        f"  Name (UPPERCASE)  : {full_name.upper()}\n"
        f"  Name (Title Case) : {full_name.title()}\n"
        f"  Age               : {info['age']} years\n"
        f"  Age in Months     : {age_in_months} months\n"
        f"  Favourite Number  : {rounded_favourite}\n"
        f"{'=' * 40}\n"
        f"\n--- Data Types ---\n"
        f"  first_name       → {type(info['first_name'])}\n"
        f"  surname          → {type(info['surname'])}\n"
        f"  age              → {type(info['age'])}\n"
        f"  favourite_number → {type(info['favourite_number'])}\n"
    )


def main():
    """Main entry point."""
    student_info = get_student_info()
    profile = format_profile(student_info)
    print(profile)


if __name__ == "__main__":
    main()