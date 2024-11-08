class Student:

    def __init__(self, name='Louie', id='000000', gpa=0.0):
        self.name = name
        self.id = id
        self.gpa = gpa

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_gpa(self):
        return self.gpa

    def set_name(self, name):
        self.name = name    

    def set_id(self, id):
        self.id = id

    def set_gpa(self, gpa):
        self.gpa = gpa
    

if __name__ == "__main__":
    initial_student = Student()
    print(f'{ initial_student.get_name() } / { initial_student.get_id() } / { initial_student.get_gpa() }')

    initial_student.set_name('Felix')
    initial_student.set_id('555555')
    initial_student.set_gpa(3.7)
    print(f'{ initial_student.get_name() } / { initial_student.get_id() } / { initial_student.get_gpa() }')