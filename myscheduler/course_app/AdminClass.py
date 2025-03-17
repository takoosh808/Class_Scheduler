from User import User
from Class import Class
from Student import Student
class Admin(User):
    def __init__(self, username: str, password: str):
        super().__init__(username, password)
    
    def CreateNewClass(self, class_list: list, class_id: str, pre_reqs: list, time: str, location: str, available_seats: int):
            new_class = Class(class_id, pre_reqs, time, location, available_seats)
            class_list.append(new_class)
            # Place holder success message
            print(f"Class {class_id} created successfully.")
    
    def ManuelEnrollStudent(self, student: Student, class_id: str): # NOT YET WORKING
        if class_id not in student.CurrentClasses:
            student.CurrentClasses.append(class_id)
            # Place hodler success message
            print(f"Enrolled {student.Name} in {class_id}.")
        else:
            # Place holder error message
            print(f"{student.Name} is already enrolled in {class_id}.")