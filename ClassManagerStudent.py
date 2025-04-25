from AdminClass import Admin
from Student import Student
from Class import Class
from models import Course, Student
import json


def CreateStudent(student_ID:str):
    obj = Student.objects.get(id_number = student_ID)
    shoppingCartList = []
    shoppingCartList += obj.shoppingCart1
    shoppingCartList += obj.shoppingCart2
    shoppingCartList += obj.shoppingCart3
    shoppingCartList += obj.shoppingCart4
    shoppingCartList += obj.shoppingCart5
    shoppingCartList += obj.shoppingCart6
    shoppingCartList += obj.shoppingCart7
    shoppingCartList += obj.shoppingCart8
    shoppingCartList += obj.shoppingCart9
    shoppingCartList += obj.shoppingCart10
    return Student(obj.id_number, obj.password, student_ID, obj.name, 1)

def CreateClass(class_id:str, pre_req:list, time:str, location:str, seats:int):
    return Class(class_id, pre_req, time, location, seats)

class ClassManagerStudent:
    def __init__(self, student_ID:str):
        self.student = CreateStudent(student_ID)# find and create student instance from student ID

# Returns true or false indicating success.
    def AddToShoppingCart(self, class_ID:str):
        return json.load(json.dumps(self.student.AddToShoppingCart(class_ID)))
        #maybe not
        #pass in class_ID as class object instead. So we can check conflict. Change student and shopping cart to store class objects, instead of class ID.

# Returns true or false indicating success.
    def RemoveFromShoppingCart(self, class_ID:str):
        return json.load(json.dumps(self.student.RemoveFromShoppingCart(class_ID)))
        #pass in class_ID as class object instead. So we can check conflict. Change student and shopping cart to store class objects, instead of class ID.

# Returns list of classes.
    def GetShoppingCart(self):
        return json.load(json.dumps(",".join(self.student.ShoppingCart.GetClasses())))
    
# Returns list of classes.
    def GetCurrentClass(self):
        return json.load(json.dumps(",".join(self.student.CurrentClasses)))

# Returns true or false indicating success.
    def DropClass(self, class_ID: str):
        return json.load(json.dumps(self.student.DropClass(class_ID)))

# Returns true or false indicating success.
    def Enroll(self):
        return json.load(json.dumps(self.student.Enroll()))

# Returns all classes with the name.
    def SearchClass(class_name:str):
        return json.load(json.dumps(Class.objects.get(class_name = class_name)))