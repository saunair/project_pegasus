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
    def __init__(self):
        self.test_grade = Grade()


if __name__ == "__main__":
    example_exam = Exam()
    example_exam.math_grade = 10
    example_exam.writing_grade = 100
    example_exam.science_grade = 12
    # None of the validators work for the self.attributes!
    print(example_exam.test_grade)
    example_exam.test_grade = -2
    # example_exam.geo_grade = -1
