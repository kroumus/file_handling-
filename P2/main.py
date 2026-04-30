from students_grade_tracker import GradeTracker

tracker = GradeTracker()
top = tracker.search_top_student('students.txt')

if top:
    print(f"The Top student is {top.name} with a GWA of {top.gwa}")