# Advanced level Option 2 - Student Info Formatter

def get_student_info() -> dict:
    """Collect and validate student information."""
    try:
        return {
            "first_name": input("Enter your first name: ").strip().title(),
            "surname": input("Enter your surname: ").strip().title(),
            "age": int(input("Enter your age: ").strip()),
            "favourite_number": float(input("Enter your favourite number: ").strip())
        }
    except ValueError as e:
        exit(f"Invalid input: {e}. Please restart and try again.")


def format_profile(info: dict) -> str:
    """Format student data into a profile card."""
    full_name = f"{info['first_name']} {info['surname']}"
    border = "=" * 40

    return (
        f"\n{border}\n"
        f"  Welcome, {full_name}!\n"
        f"  UPPERCASE   : {full_name.upper()}\n"
        f"  Title Case  : {full_name.title()}\n"
        f"  Age         : {info['age']} yrs ({info['age'] * 12} months)\n"
        f"  Fav Number  : {round(info['favourite_number'], 2)}\n"
        f"\n  Types → name: {type(full_name)}, age: {type(info['age'])}, fav: {type(info['favourite_number'])}\n"
        f"{border}\n"
    )


if __name__ == "__main__":
    print(format_profile(get_student_info()))