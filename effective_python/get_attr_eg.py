# Example for weakref & __get__ + __set__ usages.

import weakref


# Here the Grade acts like a property, but that can be resued as multiple properties to a class using this.
# This way a validator in the __set__ method doesn't have to be re-written.
class Grade:
    def __init__(self):
        # Wealref for the case the key is removed, we need this dictionary to delete the entry automatically, 
        # hence giving the interpretor more memory by removing the value associated to it.
        # Using this helps the garbage collector to kick in sooner, than just the end of the program.
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
# Hence we cannot construct this in initialization of Exam(). We have to set the properties 
# like `math_grade` after Exam() is initialized. Till then the value of the property is None.
class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()
    geo_grade = Grade()


if __name__ == "__main__":
    example_exam = Exam()
    # None of the validators work for the self.attributes created after the 
    example_exam.math_grade = 20
    
    # Make sure the instances have their own values.
    new_exam = Exam()
    assert new_exam.science_grade is None, "We haven't assigned a value yet"
    try:
        new_exam.science_grade = -200
        assert False, "Didn't raise an error for a value lower"
    except ValueError:
        print("Works as expected")
        pass
