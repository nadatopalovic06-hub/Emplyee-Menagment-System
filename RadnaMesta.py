"""
Created on Mon Dec  2 22:07:59 2024

@author: nada
"""

# loading job positions from file
def loadJobPositions():
    for line in open('radnaMesta.txt', 'r').readlines():
        if len(line) > 1:
            jp = str2JobPosition(line)
            jobPositions.append(jp)


# writes job positions back to file
# although there are usually no changes here
def saveJobPositions():
    file = open('radnaMesta.txt', 'w')
    for jp in jobPositions:
        file.write(jobPosition2str(jp))
        file.write('\n')
    file.close()
    
    
# converting a line from file into a dictionary    
def str2JobPosition(line):
    id, name = line.strip().split("|")
    jp = {'id': id,
            'name': name}
    return jp


# prepares string for writing into file
def jobPosition2str(rad):   
    return '|'.join([rad['id'], rad['name']])
    

# searches job position by name
def findJobPosition(name): 
    for jp in jobPositions:
        if jp['name'] == name:
            return True
    return False


print(__name__)  
jobPositions = []
loadJobPositions()
