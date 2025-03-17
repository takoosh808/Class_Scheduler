from User import User
from ShoppingCart import ShoppingCart
class Student(User):
    def __init__(self, username: str, password: str, student_id: str, name: str, class_standing: int):
        super().__init__(username, password)
        self.StudentID = student_id
        self.Name = name
        self.ClassStanding = class_standing
        self.ClassesTaken = []  # List of completed class IDs
        self.CurrentClasses = []  # List of currently enrolled class IDs
        self.ShoppingCart = ShoppingCart()  # List of classes in shopping cart

    def DropClasses(self, class_id: str):
        if class_id in self.CurrentClasses:
            self.CurrentClasses.remove(class_id)
            self.ClassesTaken.append(class_id)
            #Place holder for success message
        else:
            # Place holder for failed message
            print(f"Class {class_id} not found in current classes.")

    def SearchClasses(self, available_classes: list, keyword: str): #NOT YET WORKING
        # Place holder for search classes
        results = []
        return results

    def AddToShoppingCart(self, class_id: str): #NOT YET WORKING
        if class_id not in self.ShoppingCart:
            self.ShoppingCart.append(class_id)
            #Place holder for success message
        else:
            # Place holder for failed message
            print(f"Class {class_id} is already in the shopping cart.")