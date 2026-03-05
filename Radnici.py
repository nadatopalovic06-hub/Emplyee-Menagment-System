# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:44:43 2024

@author: nada
"""

from datetime import date, datetime


# loading employees from file
def loadEmployees():
    for line in open('radnici.txt', 'r').readlines():
        if len(line) > 1:
            emp = str2Employee(line)
            employees.append(emp)


# writes a new employee to the file
def saveEmployees():
    file = open('radnici.txt', 'w')
    for emp in employees:
        file.write(employee2str(emp))
        file.write('\n')
    file.close()
    

# finds an employee by id number
def findEmployee(index): 
    for emp in employees:
        if emp['id'] == index:
            return emp
    return None
    

# searches employees by last name
# field can be last name (if searching by city then field would be city)
# since multiple employees can have the same last name, it returns a list
def searchEmployees(field, value): 
    result = []
    for emp in employees:
        if emp[field].upper() == value.upper():
            result.append(emp)
    return result


# adds a new employee to the list
def addEmployee(emp): 
    employees.append(emp)
    

# updates data of a specific employee (here it changes the job position)
def updateEmployee(index, emp): 
    employees[index] = emp


# reads a line from the file and converts it into an Employee
# (assigns values to dictionary keys)
def str2Employee(line):
    id, firstName, lastName, birthDate, birthDate, email, salary, position = line.strip().split("|")
    emp = {'id': id,
            'firstName': firstName,
            'lastName': lastName,
            'birthDate': birthDate,
            'employmentDate': birthDate,
            'email': email,
            'salary': salary,
            'position': position}
    return emp


# prepares string for writing to file
def employee2str(emp):    
    return '|'.join([emp['id'], emp['firstName'], emp['lastName'], 
                     emp['birthDate'], emp['employmentDate'], 
                     emp['email'], str(emp['salary']), emp['position']])
     

# finds the next available id number
def maxId():
    return len(employees) + 1


# header for displaying employee data
def formatHeader():
    return \
      "Id  |Name    |Last name   |Birth date |Birth date |Email           |Salary       |Position\n" \
      "---+--------+------------+-----------+-----------+----------------+-------------+-----------"


def formatEmployee(emp):
    return u"{0:3}|{1:<7}|{2:10}|{3:10}|{4:10}|{5:20}|{6:>6}|{7:>10}".format(
      emp['id'],
      emp['firstName'],
      emp['lastName'],
      emp['birthDate'],
      emp['employmentDate'],
      emp['email'],
      emp['salary'],
      emp['position'])


# prints one row for each employee below the header
def formatEmployees(empList): # should be able to format any list passed to it
    return "\n".join(map(formatEmployee, empList))


# this printing could be simpler, left from a previous project
def formatAllEmployees():
    return formatEmployees(employees)


def allEmployees():
    return employees    

    
def sortEmployees(key):
    return sorted(employees, key = lambda x: x[key])
    

print(__name__)  
employees = []
loadEmployees()


