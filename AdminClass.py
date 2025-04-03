from User import User
from Class import Class
from Student import Student
from models import Course, Student
import json

def ChangeAvailableSeats(self, class_id:str, change:int):
    if Course.objects.filter(id_number = class_id).first():
        object = Course.objects.filter(id_number = class_id).first()
        object.AvailableSeats = object.AvailableSeats + change
        object.save()
        return True
    else:
         return False

class Admin(User):
    def __init__(self, username: str, password: str):
        super().__init__(username, password)
    
    #Creates a new class, returns bool indicating success.
    def CreateNewClass(self, class_id: str, name:str, date:str, pre_req1:str, pre_req2:str, pre_req3:str, time: str, location: str, available_seats: int):
            pre_req_list = []
            if pre_req1 != "None":
                 pre_req_list += pre_req1
            if pre_req2 != "None":
                 pre_req_list += pre_req2
            if pre_req3 != "None":
                 pre_req_list += pre_req3
            new_class = Class(class_id, pre_req_list, time, location, available_seats)
            if not self.CheckClassConflict(new_class):
                Course.objects.create(id_number = class_id, class_name = name, date = date, time = time, PreReqs1 = pre_req1, PreReqs2 = pre_req2, PreReqs3 = pre_req3, Location = location, AvailableSeats = available_seats)
                return json.load(json.dumps(True))
            else:
                return json.load(json.dumps(False))
            
    
    #Enroll student in class, bypassing any checks. Returns bool indicating successful or not.
    def ManuelEnrollStudent(self, student: Student, class_id: str):
        if class_id not in student.CurrentClasses:
            student.CurrentClasses.append(class_id)
            ChangeAvailableSeats(class_id, -1)
            return json.load(json.dumps(True))
        else:
            return json.load(json.dumps(False))
            
    #Check if there is a class conflict.
    def CheckClassConflict(self, class_:Class):
        if Course.objects.filter(time = class_.Time, Location = class_.Location).first():
             return True
        else:
             return False
        

             
              
