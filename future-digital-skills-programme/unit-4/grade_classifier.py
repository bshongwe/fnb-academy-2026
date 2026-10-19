# Student Grade Classifier

def display_row(label, value):
    """Helper function to print a formatted report card row."""
    print(f"{label:<30} {value}")

def get_grade(average):
    """Assigns a letter grade based on the average mark."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def get_status(average):
    """Assigns Pass/Fail status based on the average mark."""
    if average >= 50:
        return "PASS"
    else:
        return "FAIL"

def check_intervention(subject_name, mark):
    """Flags a subject if the mark is below 40."""
    if mark < 40:
        return f"{subject_name} needs intervention!"
    return None

def run_grade_classifier():
    print("\n" + "=" * 45)
    print(f"{'🎓 STUDENT GRADE CLASSIFIER 🎓':^45}")
    print("=" * 45)

    # 1. Collect learner name and marks
    name        = input("Enter learner's name: ")
    subject1    = input("Enter first subject name: ")
    mark1       = float(input(f"Enter mark for {subject1}: "))
    subject2    = input("Enter second subject name: ")
    mark2       = float(input(f"Enter mark for {subject2}: "))
    subject3    = input("Enter third subject name: ")
    mark3       = float(input(f"Enter mark for {subject3}: "))

    # 2. Calculate average
    average = round((mark1 + mark2 + mark3) / 3, 2)

    # 3. Assign grade and status
    grade   = get_grade(average)
    status  = get_status(average)

    # 4. Check for intervention flags
    interventions = []
    for subject, mark in [(subject1, mark1), (subject2, mark2), (subject3, mark3)]:
        flag = check_intervention(subject, mark)
        if flag:
            interventions.append(flag)

    # 5. Display formatted report card
    print("\n" + "=" * 45)
    print(f"{'REPORT CARD':^45}")
    print("=" * 45)
    display_row("Learner Name:", name)
    print("-" * 45)
    display_row(f"{subject1} Mark:", f"{mark1}%")
    display_row(f"{subject2} Mark:", f"{mark2}%")
    display_row(f"{subject3} Mark:", f"{mark3}%")
    print("-" * 45)
    display_row("Average Mark:", f"{average}%")
    display_row("Letter Grade:", grade)
    display_row("Status:", status)
    print("-" * 45)

    # 6. Display intervention flags
    if interventions:
        print(f"\n{'INTERVENTION REQUIRED':^45}")
        print("-" * 45)
        for flag in interventions:
            print(f"  {flag}")
    else:
        print(f"{' No Interventions Required':^45}")

    print("=" * 45)

# Run the classifier
run_grade_classifier()