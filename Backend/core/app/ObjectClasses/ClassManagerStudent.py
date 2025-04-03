from AdminClass import Admin
from Student import Student
from Class import Class
from models import Course, Student
import json


def CreateStudent(student_ID:str): #NOT YET WORKING
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

def CreateClass(class_id:str):#NOT YET WORKING
    return Class(class_id, [], "Time", "Location", 100)

class ClassManagerStudent:
    def __init__(self, student_ID:str): #pass in database?
        self.student = CreateStudent(student_ID)# find and create student instance from student ID
<<<<<<< HEAD
        self.classList = [] #read class list from database
        self.studentList = [] #read student list from database

    def AddToShoppingCart(self, class_ID:str):
        return self.student.AddToShoppingCart(class_ID)
        #maybe not
        #pass in class_ID as class object instead. So we can check conflict. Change student and shopping cart to store class objects, instead of class ID.
    
    def RemoveFromShoppingCart(self, class_ID:str):
        return self.student.RemoveFromShoppingCart(class_ID)
        #pass in class_ID as class object instead. So we can check conflict. Change student and shopping cart to store class objects, instead of class ID.
    
    def GetShoppingCart(self):
        return json.load(",".join(self.student.ShoppingCart.GetClasses()))
    
    def GetCurrentClass(self):
        return json.load(",".join(self.student.CurrentClasses))
    
    def DropClass(self, class_ID: str):
        return self.student.DropClass(class_ID)
        #Change seat avaibility

    def Enroll(self):
        return self.student.Enroll()
=======

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
        #Change seat avaibility

# Returns true or false indicating success.
    def Enroll(self):
        return json.load(json.dumps(self.student.Enroll()))
>>>>>>> ben2
        #change seat avaibility