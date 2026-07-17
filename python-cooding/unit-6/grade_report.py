# Grade report programme

def get_grade(average):
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
    return "PASS" if average >= 50 else "FAIL"


def avg_3(maths, english, science):
    return round((maths + english + science) / 3, 2)


def main():
    # At least 5 students as a list of dictionaries
    students = [
        {"name": "Amara", "maths": 78, "english": 66, "science": 84},
        {"name": "Sipho", "maths": 45, "english": 52, "science": 49},
        {"name": "Lerato", "maths": 92, "english": 88, "science": 80},
        {"name": "Thabo", "maths": 61, "english": 59, "science": 63},
        {"name": "Nandi", "maths": 30, "english": 41, "science": 55},
    ]

    results = []

    # Process each student using a for-loop
    for student in students:
        name = student["name"]
        maths = float(student["maths"])
        english = float(student["english"])
        science = float(student["science"])

        average = avg_3(maths, english, science)
        grade = get_grade(average)
        status = get_status(average)

        results.append({
            "name": name,
            "average": average,
            "grade": grade,
            "status": status
        })

    # Class statistics after the loop
    averages = [r["average"] for r in results]
    all_marks = []
    for s in students:
        all_marks.extend([float(s["maths"]), float(s["english"]), float(s["science"])])
    class_average = round(sum(averages) / len(averages), 2)
    highest_mark = round(max(all_marks), 2)
    lowest_mark = round(min(all_marks), 2)

    # Display formatted class report
    print("\n" + "=" * 60)
    print(f"{'CLASS GRADE REPORT':^60}")
    print("=" * 60)

    print(f"{'Name':<15} {'Average':<10} {'Grade':<8} {'Status':<8}")
    print("-" * 60)

    for r in results:
        print(f"{r['name']:<15} {r['average']:<10} {r['grade']:<8} {r['status']:<8}")

    print("-" * 60)
    print(f"{'Class Average:':<28}{class_average}")
    print(f"{'Highest Mark:':<28}{highest_mark}")
    print(f"{'Lowest Mark:':<28}{lowest_mark}")
    print("=" * 60)

    # While loop for searching students by name after the report is shown
    while True:
        search_name = input("\nEnter a student name to search (or type 'exit' to stop): ").strip()

        if search_name.lower() == "exit":
            print("Goodbye!")
            break

        found = None
        for r in results:
            if r["name"].lower() == search_name.lower():
                found = r
                break

        if found is None:
            print(f"Student '{search_name}' not found.")
        else:
            print("\n✅ Student found:")
            print(f"Name   : {found['name']}")
            print(f"Average: {found['average']}")
            print(f"Grade  : {found['grade']}")
            print(f"Status : {found['status']}")


if __name__ == "__main__":
    main()