class ShoppingCart:
    def __init__(self):
        self.FutureCourses = []  # List of future class IDs
    
    def AddToCart(self, class_id: str):
        if class_id not in self.FutureCourses:
            self.FutureCourses.append(class_id)
            # Place holder for success message
            print(f"Added {class_id} to the shopping cart.")
        else:
            print(f"{class_id} is already in the shopping cart.")
    
    def GenerateVisualSchedule(self): #NOT YET WORKING
        #place holder for schedule generation
        print("Visual schedule generated for:", self.FutureCourses)
    
    def EnrollClasses(self): #NOT YET WORKING - needs conflict checks
        for class_id in self.FutureCourses:
            if (True): # Place holder for conflict checks
                #Place holder success message
                print(f"Enrolled in {class_id}.")
                return self.FutureCourses
            else:
                # Place holder error message
                print(f"Already enrolled in {class_id}.")
        self.FutureCourses.clear()  # Clear cart after enrollment