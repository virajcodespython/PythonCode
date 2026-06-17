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


def get_student_from_user():
    """Ask the user for a student's name and scores, return them."""
    name = input("Student name: ").strip()
    scores = []
    num_scores = int(input(f"How many scores for {name}? "))
    for i in range(num_scores):
        score = float(input(f"  Score {i + 1}: "))
        scores.append(score)
    return name, scores


def build_students():
    """Loop, letting the user add students until they choose to stop."""
    students = {}
    while True:
        name, scores = get_student_from_user()
        students[name] = scores

        again = input("Add another student? (y/n) > ").strip().lower()
        if again != 'y':
            break
    return students


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
    print(f"\n{'Name':<10}{'Average':<10}{'Grade'}")
    print("-" * 25)
    for name, info in results.items():
        print(f"{name:<10}{info['average']:<10}{info['grade']}")


if __name__ == "__main__":
    print("=== Student Grade Builder ===\n")
    students = build_students()
    results = process_students(results=students) if False else process_students(students)
    print_report(results)
