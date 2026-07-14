# Student Info Formatter

from dataclasses import dataclass, field

@dataclass
class Student:
    """
    Represents a student and their profile
    """

    first_name      : str   = field(default_factory=lambda: input("Enter your first name: ").strip().title())
    surname         : str   = field(default_factory=lambda: input("Enter your surname: ").strip().title())
    age             : int   = field(default_factory=lambda: int(input("Enter your age: ").strip()))
    favourite_number: float = field(default_factory=lambda: float(input("Enter your favourite number: ").strip()))

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.surname}"

    def __str__(self) -> str:
        border = "=" * 40
        return (
            f"\n{border}\n"
            f"  Welcome, {self.full_name}!\n"
            f"  UPPERCASE  : {self.full_name.upper()}\n"
            f"  Title Case : {self.full_name.title()}\n"
            f"  Age        : {self.age} yrs ({self.age * 12} months)\n"
            f"  Fav Number : {round(self.favourite_number, 2)}\n"
            f"\n  Types → name: {type(self.full_name)}, "
            f"age: {type(self.age)}, fav: {type(self.favourite_number)}\n"
            f"{border}\n"
        )


if __name__ == "__main__":
    try:
        print(Student())
    except ValueError as e:
        exit(f"Invalid input: {e}. Please restart and try again.")