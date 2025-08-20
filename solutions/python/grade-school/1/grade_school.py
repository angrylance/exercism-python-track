# Solution to https://exercism.org/tracks/python/exercises/grade-school


class School:
    def __init__(self):
        self._roster = {}
        self._all_students = set()
        self._added = []

    def add_student(self, name, grade):
        if name in self._all_students:
            self._added.append(False)
        else:
            self._all_students.add(name)
            self._roster.setdefault(grade, set()).add(name)
            self._added.append(True)

    def roster(self):
        result = []
        for grade in sorted(self._roster):
            result.extend(sorted(self._roster[grade]))
        return result

    def grade(self, grade_number):
        return sorted(self._roster.get(grade_number, []))

    def added(self):
        return self._added
