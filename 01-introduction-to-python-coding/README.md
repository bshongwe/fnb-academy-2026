# Python Coding Academy

A comprehensive collection of Python programming exercises and projects organized by learning units, covering fundamental to intermediate Python concepts.

## Unit 1: Variables, Input/Output, and String Manipulation

**Concepts Covered:** Variables, user input, string methods, dataclasses, classes

### Files

- **student_info.py** - Basic student information formatter using dataclass decorator
  - Collects first name, surname, age, and favourite number
  - Displays formatted profile with uppercase, title case, and data types

- **student_info_adv.py** - Advanced functional approach
  - Separates data collection, formatting, and display logic
  - Includes error handling for invalid inputs

- **student_info_adv_class.py** - Object-oriented implementation
  - Uses class-based structure with properties
  - Implements `__str__` method for formatted output

- **student_info_adv_data-class.py** - Dataclass-based solution
  - Combines dataclass benefits with advanced formatting
  - Uses `field(default_factory=...)` for input handling

- **unit-1-challenge_concert-ticket-booker.py** - Challenge project
  - Concert ticket booking confirmation system
  - Input validation and string formatting

## Unit 2: String Formatting and Manipulation

**Concepts Covered:** String slicing, concatenation, f-strings, string methods

### Files

- **string-formatter.py** - Username and message formatter
  - Generates username from first initial + last name
  - Formats full name with title case
  - Bio cleaning and character counting
  - String replacement operations

- **string-formatter-2.py** - Advanced string formatting variant

- **unit-2-challenge_password-hint-tool.py** - Challenge project
  - Secure password hint generator
  - Extracts first and last letters
  - Case conversion for hints

## Unit 3: Arithmetic Operations and Calculations

**Concepts Covered:** Mathematical operations, type casting, rounding, formatted output

### Files

- **calculator.py** - Multi-function calculator
  - Performs addition, subtraction, multiplication
  - Handles division, floor division, and modulus
  - Division by zero error handling
  - Formatted table output with helper functions

- **fuel_cost_calculator.py** - South African fuel cost calculator
  - Calculates fuel consumption (1L per 10km)
  - Computes total trip cost in ZAR
  - Formatted trip summary display

## Unit 4: Conditional Logic and Control Flow

**Concepts Covered:** If-elif-else statements, comparison operators, boolean logic

### Files

- **grade_classifier.py** - Student grade classification system
  - Calculates average from three subjects
  - Assigns letter grades (A-F) based on thresholds
  - Determines pass/fail status
  - Flags subjects needing intervention (marks < 40)
  - Generates formatted report card

- **atm_simulator.py** - ATM withdrawal simulator
  - Validates withdrawal amounts
  - Checks for sufficient funds
  - Handles invalid and zero amounts
  - Displays remaining balance

## Unit 5: Lists, Dictionaries, and Data Structures

**Concepts Covered:** Lists, dictionaries, CRUD operations, menu-driven programs

### Files

- **contact_book.py** - Command-line contact management system
  - Add new contacts with name, phone, and email
  - Search contacts by name (case-insensitive)
  - Delete contacts
  - View all contacts in formatted layout
  - Prevents duplicate contact names

- **high_score_tracker.py** - Game score tracking system
  - Tracks highest score across multiple entries
  - Accepts scores until user types 'stop'
  - Provides feedback on performance
  - Displays best score at session end

## Unit 6: Loops and Advanced Data Processing

**Concepts Covered:** For loops, while loops, list comprehensions, data aggregation

### Files

- **grade_report.py** - Class grade report generator
  - Processes multiple students from list of dictionaries
  - Calculates individual averages and grades
  - Computes class statistics (average, highest, lowest marks)
  - Interactive student search functionality
  - Formatted tabular report display

- **phone_directory_search.py** - Phone directory lookup tool
  - Combines dictionary and list data structures
  - Case-sensitive contact search
  - Simple lookup interface

## Key Programming Concepts

### Across All Units
- **Input/Output:** User input collection and validation
- **Data Types:** Strings, integers, floats, booleans
- **Type Casting:** Converting between data types
- **Error Handling:** Try-except blocks for invalid inputs
- **String Methods:** `.strip()`, `.lower()`, `.upper()`, `.title()`, `.replace()`
- **Formatted Output:** f-strings, alignment, padding, separators

### Data Structures
- **Variables:** Basic data storage
- **Lists:** Ordered collections (Unit 5-6)
- **Dictionaries:** Key-value pairs (Unit 5-6)
- **Dataclasses:** Structured data objects (Unit 1)

### Control Flow
- **Conditional Statements:** if-elif-else (Unit 4)
- **Loops:** while loops (Unit 5-6), for loops (Unit 6)
- **Functions:** Definition, parameters, return values (Units 3-6)
- **Properties:** Computed attributes (Unit 1)

### Advanced Features
- **List Comprehensions:** Efficient data processing (Unit 6)
- **Dictionary Operations:** CRUD on key-value data (Unit 5-6)
- **Modular Design:** Functions with single responsibilities
- **User Experience:** Menu systems, validation, formatted displays

## Running the Programs

All Python files are standalone scripts. To run any program:

```bash
python python-cooding/unit-X/filename.py
```

Replace `unit-X` with the appropriate unit number and `filename.py` with the desired script.

## Learning Path

1. **Start with Unit 1** - Master variables, input/output, and basic string operations
2. **Progress to Unit 2** - Deepen string manipulation skills
3. **Advance to Unit 3** - Learn arithmetic operations and calculations
4. **Continue with Unit 4** - Understand conditional logic
5. **Explore Unit 5** - Work with lists and dictionaries
6. **Complete Unit 6** - Apply loops and advanced data processing

Each unit builds upon concepts from previous units, creating a progressive learning experience.

## Notes

- All programs use interactive command-line input
- Input validation is implemented in most scripts
- Formatted output uses consistent styling with borders and alignment
- Challenge projects apply unit concepts to real-world scenarios
- Code follows Python best practices with docstrings and type hints where applicable