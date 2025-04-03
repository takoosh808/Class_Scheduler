from User import User
from ShoppingCart import ShoppingCart
from Class import Class
<<<<<<< HEAD
=======
from AdminClass import ChangeAvailableSeats
>>>>>>> ben2
class Student(User):
    def __init__(self, username: str, password: str, student_id: str, name: str, class_standing: int, shopping_Cart:list):
        super().__init__(username, password)
        self.StudentID = student_id
        self.Name = name
        self.ClassStanding = class_standing
        self.ClassesTaken = []  # List of completed class IDs
        self.CurrentClasses = []  # List of currently enrolled class IDs
        self.ShoppingCart = ShoppingCart()  # List of classes in shopping cart
        for course in shopping_Cart:
            self.AddToShoppingCart(course)

    # Returns the contents of shopping cart, in a string.
    # def GetShoppingCart(self):
    #     return ",".join(self.ShoppingCart.GetClasses())

    # Drops a class given the course ID. Returns bool indicating whether successful or not.
    def DropClass(self, class_id: str):
        if class_id in self.CurrentClasses:
            self.CurrentClasses.remove(class_id)
<<<<<<< HEAD
=======
            ChangeAvailableSeats(class_id, 1)
>>>>>>> ben2
            return True
        else:
            return False

    # def SearchClasses(self, available_classes: list, keyword: str): #NOT YET WORKING
    #     # Place holder for search classes
    #     results = []
    #     return results

    # Adds a course to shopping cart given a class ID. Returns bool indicating whether successful or not.
    def AddToShoppingCart(self, class_id : str):
        return self.ShoppingCart.AddToCart(class_id)
    
    # Removes a class from shopping cart given class ID. Returns a bool indicating success.
    def RemoveFromShoppingCart(self, class_id: str):
        return self.ShoppingCart.RemoveClass(class_id)

    # Enroll in classes in shopping cart. Returns bool indicating whether enrollment successful or not.
    def Enroll(self): # NEEDS TO CHECK TIME CONFLICT AGAIN
        if not self.ShoppingCart.CheckClassConflict():
            for class_id in self.ShoppingCart.FutureCourses:
                if class_id in self.CurrentClasses:
                    return False
<<<<<<< HEAD
=======
                else:
                    ChangeAvailableSeats(class_id, -1)
>>>>>>> ben2
            self.CurrentClasses = self.ShoppingCart.FutureCourses
            self.ShoppingCart.ClearCart()
            return True
        else:
<<<<<<< HEAD
            return False
=======
            return False
>>>>>>> ben2
