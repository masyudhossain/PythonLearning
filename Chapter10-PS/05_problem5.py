""" 
Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways.
"""
from random import randint

class Train:
    def __init__(self,trainNo,totalSeat):
        self.trainNo = trainNo
        self.totalSeat = totalSeat
    def book(self,source, destination):
        print(f"Ticket is booked in train no: {self.trainNo} from {source} to {destination}")
    def getStatus(self):
        print(f"Seat available are {self.totalSeat}")
    def getFare(self,source, destination):
        print(f"Ticket fare in train no: {self.trainNo} from {source} to {destination} is {randint(200,2000)}")
        
t = Train(15849,250)
t.book("Kolkata","Delhi")
t.getStatus()
t.getFare("Kolkata","Delhi")

