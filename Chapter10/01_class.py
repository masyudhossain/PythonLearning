class Employee1:
    name = "Masyud"
    salary = 9000000
    role = "Backend"
    
ob = Employee1()
print(ob.name,ob.salary, ob.role)

class Employee:
    role ="DevOps" #Class attribute
    salary = 9000000
    
ob1 = Employee()
ob1.name = "Masyud" #Instance Attribute
ob1.role = "Architect"
print(ob1.name,ob1.role,ob1.salary)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class