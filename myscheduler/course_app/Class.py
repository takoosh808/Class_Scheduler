class Class:
    def __init__(self, class_id: str, pre_reqs: list, time: str, location: str, available_seats: int):
        self.ClassID = class_id
        self.PreReqs = pre_reqs
        self.Time = time
        self.Location = location
        self.AvailableSeats = available_seats
    
    def GetPreReq(self):
        return self.PreReqs
    
    def GetTime(self):
        return self.Time
    
    def GetLocation(self):
        return self.Location
    
    def ChangeAvailableSeats(self, change: int):
        self.AvailableSeats += change

    def CheckCoursePre_Reqs(self, pre_req: list):
        return all(item in pre_req for item in self.PreReqs)
