# Create a class “Programmer” for storing information of few programmers working at Microsoft
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


m = Programmer("Masyud", 1200000, 700136)
print(m.name, m.salary, m.pin, m.company)
r = Programmer("Rohan", 1200000, 245001)
print(r.name, r.salary, r.pin, r.company)
t=Programmer("Tanweer",1119999,743259)
print(t.name, t.salary, t.pin, t.company)
