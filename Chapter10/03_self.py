class Employee:
    salary = 9000000
    role = "Backend"
    
    def getInfo(self):
        print(f"The Designation is {self.role}. The salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("Good Afternoon")
ob = Employee()
ob.getInfo()
ob.greet()
# Employee.getInfo(ob)