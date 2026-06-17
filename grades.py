def calculate_average(scores):
    """Return the average of a list of scores."""
    return sum(scores) / len(scores)


def letter_grade(score):
    """Convert a numeric score to a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def process_students(students):
    """Loop through students, compute their average and grade."""
    results = {}
    for name, scores in students.items():
        avg = calculate_average(scores)
        grade = letter_grade(avg)
        results[name] = {"average": round(avg, 1), "grade": grade}
    return results


def print_report(results):
    """Display a formatted report of student results."""
    print(f"{'Name':<10}{'Average':<10}{'Grade'}")
    print("-" * 25)
    for name, info in results.items():
        print(f"{name:<10}{info['average']:<10}{info['grade']}")


if __name__ == "__main__":
    students = {
        "Alice": [88, 92, 79],
        "Bob": [65, 70, 60],
        "Charlie": [95, 89, 93],
        "Dana": [55, 60, 58],
    }

    results = process_students(students)
    print_report(results)
