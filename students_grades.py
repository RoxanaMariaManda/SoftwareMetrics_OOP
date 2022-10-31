'''
This Python file contains the object-oriented programming version of the following problem statement.

Given known information about the students of a University at the end of an academic year, namely personal information
such as unique indetifiers and their grades, this app is intended to help with the good record keeping for the admin
teams. While building this app, we are aiming for the following utilities:
    - list all students;
    - identify the passing and failing students;
    - given a certain grade threshold, identify the students below and above that grade;
    - show the students that have obtained a bursary;
    - order the failing students based on the number of resits;
    - order the students based on the grade from a certain class;

Note: The output of the programm will be easily writtable and readable from txt files. 
Note: All exceptions will be correctly raised with a friendly user readable message.
'''

### ------------------- STRUCTURE EXAMPLE --------------------------- ###

class Student:  # parent class for the different types of students

    def __init__(self, name, age, disability, dissertation, scholarship, average_grade):
        """Initialize student

        Args:
            name (str): Name of student
            age (int): Age of student
            disability (bool): Whether a student has a disability or not
            dissertation (float): Grade of the final project/dissertation
            scholarship (bool): Whether a student has a scholarship or not
            average_grade (float): The average grade for the student at at that moment in time
        """
        self.name = name
        self.age = age
        self.__disability = disability  # private method to protect the information from being accessed
        self.dissertation = dissertation
        self.scholarship = scholarship
        self.average_grade = average_grade

    def finalGrade(self):   # calculate the overall grade for a student
        """
            Calculate the final grade for the student based on grades obtained up to that point. 
            This method would be updated once the student receives more grades. 
        """
        pass

    def passFail(self, **kwargs):
        """
            *kwargs (floats): Replaced by the grades obtained by the students. 
            Check whether a student has a higher grade than the passing threshold. 
        """
        pass


class Software(Student):  # child of parent class Student
    pathway = 'Software'

    def __init__(self, input):
        """Initialise Software Student

        Args:
            homework (float): Average grade for the homework. Potentially to be further divided into multiple grades. 
            project1 (float): Grade for Project 1 
            midterm (float): Grade for Project 2
            project2 (float): Grade for Project 3
            dissertation (float): Inherited from parent class Student
        """
        super().__init__()
        self.homework = input('Homework Grade')
        self.project1 = input('Project 1 Grade')
        self.midterm = input('Midterm Exam Grad')
        self.project2 = input('Project 2 Grade')

    def passFail(self, **kwargs):
        super(Student,self).passFail(**kwargs)

    # class and factory methods
    def printPathway(cls):
        print(f'This student is part of the {cls.pathway} pathway')

class Data(Student):
    pathway = 'Data'

    def __init__(self, input):
        super().__init__()
        self.class_1 = input('Class 1 Grade')
        self.class_2 = input('Class 2 Grade')
        self.class_3 = input('CLass 3 Grade')

    def passFail(self, **kwargs):
        super(Student, self).passFail(**kwargs)


    # class and factory methods
    def printPathway(cls):
        print(f'This student is part of the {cls.pathway} pathway')

class Year():   # class that categorises the students based on the Year of study
    pass_grade = 5

    def __init__(self, students, n_scholars):
        self.students = students
        self.n_scholars = n_scholars


class Course(): # class that contains all students in an academic year for one course

    def __init__(self, students):
        self.students = students

    def orderStudentsByGrade(self):
        pass


### Define generator and iterator classes to iterate over students and grades

class Iterate(object):
    def __init__(self, iterable_name):
        self.iterable_name = iterable_name
        self.iter_name_obj = iter(iterable_name)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                next_obj = next(self.iter_obj)
                return next_obj
            except StopIteration:
                self.iter_name_obj = iter(self.iterable)

class FileHandler:
    def __init__(self,filename = None):
        self.file = open(filename)
        self.lines = [line.strip() for line in self.file.readlines()]

    def writeFile(cls):
        pass

    def readFile(cls):
        pass