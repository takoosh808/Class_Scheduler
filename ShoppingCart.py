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

    def CheckClassConflict(self):
        return len(self.FutureCourses) == len(set(self.FutureCourses))
    
    def ClearCart(self):
        self.FutureCourses = []
