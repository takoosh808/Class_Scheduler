from AdminClass import Admin
from Student import Student
from Class import Class

def CreateStudent(student_ID:str): #NOT YET WORKING
    return Student("Username", "Password", student_ID, "Name", 1)

def CreateClass(class_id:str):#NOT YET WORKING
    return Class(class_id, [], "Time", "Location", 100)

class ClassManagerStudent:
    def __init__(self, student_ID:str): #pass in database?
        self.student = CreateStudent(student_ID)# find and create student instance from student ID
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
        return ",".join(self.student.ShoppingCart.GetClasses())
    
    def GetCurrentClass(self):
        return ",".join(self.student.CurrentClasses)
    
    def DropClass(self, class_ID: str):
        return self.student.DropClass(class_ID)
        #Change seat avaibility

    def Enroll(self):
        return self.student.Enroll()
        #change seat avaibility