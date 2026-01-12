class Employee:    
    def __init__(self,name, salary,role): # dunder method which automatically called 
        self.name=name
        self.role=role
        self.salary=salary
    
    def getInfo(self):
        print(f"{self.name} is a {self.role} Engineer at Martian Corporation and salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Afternoon")
        
        
ob = Employee("Masyud",1400000,"DevOps")
ob.getInfo()
ob = Employee("Tanweer",1400000,"FullStack")
ob.getInfo()