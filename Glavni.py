"""
Created on Sun Dec  1 21:46:17 2024

@author: nada
"""

import Korisnici
import Radnici
import RadnaMesta
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
import statistics
from datetime import datetime

# job positions act only as a reference list

def main():
    print()
    print("Employee Records")
    print("====================")
    print()
    if not login():
        print("\nInvalid username or password!")
        return
    command = '0'
    while command != 'X':
        command = menu()
        if command == '1':
            findEmployee()
        elif command == '2':
            searchEmployees()
        elif command == '3':
            listEmployees()
        elif command == '4':
            updateEmployee()
        elif command == '5':
            addEmployee()
        elif command == '6':
            averageSalary()
        elif command == '7':
            employeeSalaries()
        elif command == '8':
            salaryIncrease()
        elif command == '9':
            employmentLength()
    print("Goodbye.")


def menu():
    printMenu()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'X'):
        print("\nInvalid command.\n")
        printMenu()
        command = input(">> ")
    return command.upper()


def printMenu():
    print("\nChoose an option:")
    print("  1 - find employee")
    print("  2 - search employees")
    print("  3 - list all employees")
    print("  4 - update employee data")
    print("  5 - add new employee")
    print("  6 - average salary")
    print("  7 - employee salaries")
    print("  8 - salary increase")
    print("  9 - employment length")
    print("  x - exit program")


def login():
    username = input("Username >> ")
    password = input("Password >> ")
    return Korisnici.login(username, password)


# id number should be unique,
# therefore only one employee should be found
def findEmployee():
    print("[1] Find employee\n")
    id = input("Enter id number: ")
    emp = Radnici.findRadnik(id)
    if emp != None:
        print(Radnici.formatHeader())
        print(Radnici.formatRadnik(emp))
    else:
        print("No employee with id number", id)


# multiple employees can have the same last name
def searchEmployees():
    print("[2] Search employees\n")
    lastName = input("Enter last name: ")
    empList = Radnici.searchRadniks('prezime', lastName)
    if len(empList) == 0:
        print("No employees found.")
    else:
        print(Radnici.formatHeader())
        print(Radnici.formatRadniks(empList))


# displaying all employees
def listEmployees():
    print("[3] List of all employees sorted by last name\n")
    Radnici.sortirajRadnike('prezime')
    print(Radnici.formatHeader())
    print(Radnici.formatAllRadniks())


# change employee job position
# checks if the entered job position exists
def updateEmployee():
    print("[4] Update employee data\n")
    id = input("Enter employee id >> ")
    emp = Radnici.findRadnik(id)
    if emp == None:
        print("Employee with this id does not exist.")
    else:
        print(Radnici.formatHeader())
        print(Radnici.formatRadnik(emp)) 
        jobPosition = input("Enter new job position: ")
        while not(RadnaMesta.findRadnoMesto(jobPosition)):
            jobPosition = input("Enter new job position: ")
        emp['radnoMesto'] = jobPosition
        Radnici.saveRadniks()
        

# adding a new employee
# next available id is used
def addEmployee():
    print("[5] Add new employee\n")
    emp = {}
    id = Radnici.maxId()
    emp['id'] = str(id)
    emp['ime'] = input("Enter name: ")
    emp['prezime'] = input("Enter last name: ")
    emp['datumRodjenja'] = input("Enter birth date: ")
    emp['datumZaposlenja'] = input("Enter employment date: ")
    emp['email'] = input("Enter email: ")
    emp['plata'] = input("Enter salary: ")
    jobPosition = input("Enter job position: ")
    if not(RadnaMesta.findRadnoMesto(jobPosition)):
        jobPosition = ''
    emp['radnoMesto'] = jobPosition
    Radnici.addRadnik(emp)
    Radnici.saveRadniks()
    

# average salary of all employees
def averageSalary():
    print("[6] Average salary\n")
    employees = Radnici.sviRadnici()
    salaries = []
    for r in employees:
        salaries.append(float(r['plata']))
    avg = statistics.mean(salaries)
    print('Average salary is:', avg)


# displaying employee salaries on a bar chart
def employeeSalaries():
    print("[7] Employee salaries\n")
    employees = Radnici.sviRadnici()
    names = []
    salaries = []
    for r in employees:
        names.append(r['ime'] + ' ' + r['prezime'])
        salaries.append(float(r['plata']))
    plt.bar(names, salaries)
    plt.xticks(rotation=30)
    plt.show()
    

# salary increase of 10% for employees working more than one year
def salaryIncrease():
    print("[8] Salary increase\n")
    employees = Radnici.sviRadnici()
    current_year = datetime.today().year
    current_month = datetime.today().month
    for r in employees:
        parts = r['datumZaposlenja'].split("-")
        year_employed = int(parts[0])
        month_employed = int(parts[1])
        months_of_service = (current_year - year_employed)*12 + (current_month - month_employed)
        if months_of_service >= 12:
            new_salary = float(r['plata']) * 1.1
            r['plata'] = str(round(new_salary,2))
        Radnici.saveRadniks()


# employment length in years        
def employmentLength():
    print("[9] Employment length\n")
    employees = Radnici.sviRadnici()
    current_year = datetime.today().year
    names = []
    years = []
    for r in employees:
        year_employed = int(r['datumZaposlenja'].split("-")[0])
        service = current_year - year_employed
        names.append(r['ime'] + " " + r['prezime'])
        years.append(service)
        
    plt.bar(names, years)
    plt.xticks(rotation=30)
    plt.show()
    

print(__name__)    
if __name__ == '__main__':
    main()
