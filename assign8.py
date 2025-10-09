# gpa_system.py

class InvalidGradeError(Exception):
    """Custom exception for invalid grade values."""
    pass


class Course:
    def __init__(self, name: str, credits: int):
        self.name = name
        self.credits = credits


class Grade:
    # Grade points mapping (common GPA scale)
    GRADE_POINTS = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }

    def __init__(self, course: Course, grade: str):
        if grade not in Grade.GRADE_POINTS:
            raise InvalidGradeError(f"Invalid grade: {grade}")
        self.course = course
        self.grade = grade
        self.points = Grade.GRADE_POINTS[grade]


class Student:
    def __init__(self, name: str):
        self.name = name
        self.grades = []

    def add_grade(self, course: Course, grade_value: str):
        """Assign a grade to the student for a course."""
        grade = Grade(course, grade_value)
        self.grades.append(grade)

    def calculate_gpa(self) -> float:
        """Calculate GPA based on course grades."""
        if not self.grades:
            return 0.0

        total_points = sum(g.points * g.course.credits for g in self.grades)
        total_credits = sum(g.course.credits for g in self.grades)
        return round(total_points / total_credits, 2)

    def generate_transcript(self) -> str:
        """Return a formatted transcript string."""
        transcript = f"Transcript for {self.name}\n"
        transcript += "-" * 30 + "\n"
        for g in self.grades:
            transcript += f"{g.course.name} ({g.course.credits} credits): {g.grade}\n"
        transcript += f"GPA: {self.calculate_gpa()}\n"
        return transcript
