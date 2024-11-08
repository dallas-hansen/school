class Student:

    def __init__(self):
        self.__name = ''
        self.__id = ''
        self.__gpa = 0.0

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_gpa(self):
        return self.__gpa

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_gpa(self, gpa):
        self.__gpa = gpa
    

if __name__ == "__main__":
    initial_student = Student()
    print(f'{ initial_student.get_name() } / { initial_student.get_id() } / { initial_student.get_gpa() }')

    initial_student.set_name('Felix')
    initial_student.set_id('555555')
    initial_student.set_gpa(3.7)
    print(f'{ initial_student.get_name() } / { initial_student.get_id() } / { initial_student.get_gpa() }')
