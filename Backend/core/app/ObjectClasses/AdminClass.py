from User import User
from Class import Class
from Student import Student
from models import Course, Student
class Admin(User):
    def __init__(self, username: str, password: str):
        super().__init__(username, password)
    
    #NOT YET WORKING, needs to check conflicts
    def CreateNewClass(self, class_list: list, class_id: str, pre_reqs: list, time: str, location: str, available_seats: int):
            new_class = Class(class_id, pre_reqs, time, location, available_seats)
            if not self.CheckClassConflict(new_class):
                class_list.append(new_class)
                return True
            else:
                return False
            
    
    #Enroll student in class, bypassing any checks. Returns bool indicating successful or not.
    def ManuelEnrollStudent(self, student: Student, class_id: str):
        if class_id not in student.CurrentClasses:
            student.CurrentClasses.append(class_id)
            return True
        else:
            return False
        
    def CheckClassConflict(self, class_:Class):#NOT YET DONE
         return False