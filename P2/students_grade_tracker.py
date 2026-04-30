class Student:
    def __init__(self, name, gwa):
        self.name = name
        self.gwa = float(gwa)
class GradeTracker:
    def search_top_student(self, file_name):
        top_student = None

        with open(file_name, 'r') as file:
            for line in file:
                name, gwa = line.strip().split(',')
                current_student = Student(name, gwa)
        
                if top_student is None or current_student.gwa < top_student.gwa:
                    top_student = current_student
        return top_student