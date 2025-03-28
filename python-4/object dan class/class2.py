#sample class2.py 
class Employee: 
    'Common base class for all employees' 
    empCount = 0 

    def _init__(self, nama, salary): 
        self.nama = nama 
        self.salary = salary 
        Employee.empCount += 1
         
    def displayCount(self): 
        print("Total Employee %d" % Employee.empCount) 

    def displayEmployee (self): 
        print("Nama", self.nama, ", Salary: ", self.salary) 

# This would create first object of Employee class 
emp1 = Employee("Udin", 2000) 
# This would create second object of Employee class 
emp2 = Employee ("Manni", 5000) 

emp1.displayEmployee() 
emp2.displayEmployee() 
print("Total Employee %d" % Employee.empCount)

print("© by FEBRIANA_006") 