#!/usr/bin/python
import pickle
import os
class Person(object):
    __adhaar_no = 1
    def __init__(self, name, dob, gender):
        self.__adhaar_no = Person.__adhaar_no
        Person.__adhaar_no += 1
        self.__name = name
        self.__dob = dob
        self.__gender = gender
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def changeDOB(self, dob):
        self.__dob = dob
    def getDOB(self):
        return self.__dob
    def __str__(self):
        return "" #string form of object

class Employee(Person):
    def __init__(self, eid, name, dob, gender, salary, exp, designation):
        Person.__init__(self, name, dob, gender)
        self.eid = eid
        self.salary = salary
        self.exp = exp
        self.designation = designation
    
class Company(object):
    company_id = 1
    def __init__(self, name, address, owner_name, owner_dob, owner_gender, pan_no, active_emp = 'active_employee.txt', inactive_emp ='inactive_employee.txt'):
        self.name = name
        self.address = address
        self.pan_no = pan_no
        self.employees = {}
        self.resigned_employees = {}
        self.active_emp = active_emp
        self.inactive_emp = inactive_emp
        if not os.path.exists(active_emp):
            print("no employees exists")
            self.employee_id = 1
            owner = Employee(self.employee_id, owner_name, owner_dob, owner_gender, 10000000, 2, "CEO")
            self.employees[self.employee_id] = owner
        else:
            print("employees exists hence loading")
            self.Load()
    def Save(self):
        fd = open(self.active_emp, "wb")
        for emp in self.employees:
            pickle.dump(self.employees[emp], fd)
        fd.close()
    def Load(self):
        fd = open(self.active_emp, "rb")
        try:
            while True:
                emp = pickle.load(fd)
                print(emp.__dict__)
                self.employees[emp.eid] = emp
        except:
            pass

    def AddEmployee(self, name, dob, gender, salary, experience, designation):
        self.employee_id += 1
        emp = Employee(self.employee_id, name, dob, gender, salary, experience, designation)
        self.employees[self.employee_id] = emp

    def DeleteEmployee(self, employee_id):
        if employee_id in self.employees:
            print("Employee has resigned adding to resigned database.")
            self.resigned_employees[employee_id] = self.employees[employee_id]
            del self.employees[employee_id]

    def UpdateEmployee(self, employee_id, **update_attributes):
        if employee_id in self.employees:
            emp = self.employees[employee_id]
            for key in update_attributes:
                if key == "name":
                    emp.setName(update_attributes[key])
                elif key == "salary":
                    emp.salary = salary
        else:
            print("Employee Not Found...")

    def SearchEmployee(self, employee_id):
        if employee_id in self.employees:
            print("Current Employee")
            return self.employees[employee_id]
        elif employee_id in self.resigned_employees:
            print("Resigned Employee")
            return self.resigned_employees[employee_id]
        return None

    def Display(self):
        for emp_id in self.employees:
            emp = self.employees[emp_id]
            print(emp.eid, emp.getName())
def main():
    persistent_sys = Company("Persistent Systems Ltd", "S.B Road", "Dr Anand Deshpande", "1-1-1955", 'Male', 'asdfndslf')  
    # Menu Driven Program for Employee Management of Persistent Systems
    '''
    persistent_sys.AddEmployee("Gopal", "21-03-1990", "Male", "500000", 4, "Sr Engineer")  
    persistent_sys.AddEmployee("Yogesh", "01-05-1984", "Male", "5000000", 8, "VP")  
    persistent_sys.AddEmployee("Kamlakar", "13-11-1993", "Male", "50000", 2, "Engineer")  
    persistent_sys.AddEmployee("Mangesh", "29-12-1996", "Male", "25000", 0, "Associate Engineer")  
    persistent_sys.Display()
    
    persistent_sys.UpdateEmployee(5, name="Prafulla")

    persistent_sys.Display()
    
    persistent_sys.DeleteEmployee(3)
    
    persistent_sys.Display()
    
    emp = persistent_sys.SearchEmployee(3)
    persistent_sys.Save()
    persistent_sys.Load()
    '''
if __name__ == "__main__":
    main()
