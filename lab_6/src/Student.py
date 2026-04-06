class Student:
    def __init__(
        self,
        name: str, 
        group: str, 
        average_grade: float
    ) -> None:
        
        self.name = name
        self.group = group
        self.average_grade = average_grade


    def __str__(self) -> str:
        return f"Student: Name - {self.name}, Group - {self.group}, Average_grade - {self.average_grade}"

    def __repr__(self) -> str:
        return f"Student: name = '{self.name}', group = '{self.group}', average_grade = {self.average_grade})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return False
        return (
            self.name == other.name and
            self.group == other.group and
            self.average_grade == other.average_grade
        )

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Student):
            raise TypeError("Cannot compare Student with non-Student")
        return self.average_grade < other.average_grade