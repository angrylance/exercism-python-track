# Solution to https://exercism.org/tracks/python/exercises/grade-school


class School:
    """
    Represents a school roster that stores students grouped by grades.
    Provides functionality to add students, check which students were added
    successfully, and retrieve students either by grade or as a full sorted roster.
    """

    def __init__(self):
        """
        Initialize a new empty school roster.
        """
        self._roster = {}
        self._all_students = set()
        self._added = []

    def add_student(self, name: str, grade: int) -> None:
        """
        Add a student to the school roster.
        A student can only be added once to the entire school.
        Subsequent attempts to add the same student will be rejected.
        Args:
            name (str): The name of the student.
            grade (int): The grade to which the student belongs.
        Side Effects:
            Updates internal roster and the history of addition attempts.
        """
        if name in self._all_students:
            self._added.append(False)
        else:
            self._all_students.add(name)
            self._roster.setdefault(grade, set()).add(name)
            self._added.append(True)

    def roster(self) -> list[str]:
        """
        Return the full sorted roster of students.
        Students are sorted first by grade in ascending order,
        then by name in alphabetical order.
        Returns:
            list[str]: Sorted list of all student names in the school.
        """
        result = []
        for grade in sorted(self._roster):
            result.extend(sorted(self._roster[grade]))
        return result

    def grade(self, grade_number: int) -> list[str]:
        """
         Return the list of students in a given grade.
        The students are sorted alphabetically.
        Args:
            grade_number (int): The grade to look up.
        Returns:
            list[str]: Sorted list of student names in the specified grade.
        """
        return sorted(self._roster.get(grade_number, []))

    def added(self) -> list[bool]:
        """
        Return the history of addition attempts.
        Each entry corresponds to the result of a call to `add_student`.
        Returns:
            list[bool]: List of booleans where True indicates
            that the student was successfully added, and False otherwise.
        """
        return self._added
