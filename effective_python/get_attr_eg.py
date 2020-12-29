import weakref


class Grade:
    def __init__(self):
        self._values = weakref.WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
            return self  # Why?
        self._values.get(instance, None)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self._values[instance] = value


# The get / set methods work i.e. the validator works only on class attributes
class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()
    geo_grade = Grade()
    def __init__(self, math, writing, geo, science):
        self.math_grade = math
        self.writing_grade = writing
        self.science_grade = science
        self.geo_grade = geo 


if __name__ == "__main__":
    example_exam = Exam(
        math=10,
        writing=20,
        geo=30,
        science=50
    )
    example_exam.science_grade = 10
    # None of the validators work for the self.attributes created after the 
    example_exam.new_subject_grade = -200
