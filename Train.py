# write a class train which has methods to book a ticket, get status of seats and fair infirmation of the train 

class Train():
    def __init__(self, name, fare, seats): # constructor with parameters 
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("*************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("*************")

    def fareInfo(self):
        print(f"The price of the ticket is Rs {self.fare}")

    def bookTicket(self):
        if (self.seats> 0):
            print(f"Your tickets is booked and your seat no is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Train is full")

intercity = Train("Intercity Express", 30, 2) # object created

intercity.getStatus() 
intercity.fareInfo()
intercity.bookTicket()
intercity.getStatus() 
