#sample class.py 
class Employee: 
    'Common base class for all employees' 
    empCount = 0 

    def __init__(self, nama, salary): 
        self.nama = nama 
        self.salary = salary 
        Employee.empCount += 1 

    def displayCount (self): 
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee (self) :
        print ("Nama:", self.nama, ", Salary:", self.salary)

print("© by FEBRIANA_006") 