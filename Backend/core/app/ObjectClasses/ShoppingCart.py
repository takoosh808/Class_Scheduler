from Class import Class

class ShoppingCart:
    def __init__(self):
        self.FutureCourses = []  # List of future class IDs
    
    # Adds class to shopping cart given class ID. Returns bool indicating if class was added.
    def AddToCart(self, class_id: str):
        if class_id not in self.FutureCourses:
            self.FutureCourses.append(class_id)
            return True
        else:
            return False
    
    #Removes a class from shopping cart given class ID. Returns bool indicating success.
    def RemoveClass(self, class_id:str):
        if class_id in self.FutureCourses:
            self.FutureCourses.remove(class_id)
            return True
        else:
            return False
    
    # Returns list of future course IDs.
    def GetClasses(self):
        return self.FutureCourses

    def CheckClassConflict(self): #NOT YET WORKING - returns if there is class time conflicts
        return False
    
    def ClearCart(self):
        self.FutureCourses = []

        

    # def EnrollClasses(self): #NOT YET WORKING - needs conflict checks
    #     for class_id in self.FutureCourses:
    #         if (True): # Place holder for conflict checks
    #             #Place holder success message
    #             print(f"Enrolled in {class_id}.")
    #             return self.FutureCourses
    #         else:
    #             # Place holder error message
    #             print(f"Already enrolled in {class_id}.")
    #     self.FutureCourses.clear()  # Clear cart after enrollment