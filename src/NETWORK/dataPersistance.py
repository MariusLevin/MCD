# LIBRAIRY
import csv

# FUNCTIONS
def saveData(dictionary):
    with open('../../data/data.txt', 'w') as f:
        for key, value in d.items():
            f.write('%s:%s\n' % (key, value))

def loadData():
    dictionary = {}
    with open('../../data/data.txt') as r:
        for item in r:
            if ':' in item:
                key, value = item.split(':', 1)
                value = value.replace('\'', '')
                value = value.replace(' ', '')
                value = value.replace('\n', '')
                value = value.replace('[', '')
                value = value.replace(']', '')
                value = value.split(',')
                dictionary[key] = value
            else:
                pass # deal with bad lines of text here
    return dictionary

# TESTS
d = {'key1': [], 'key2': ['1', '2', '3']}
saveData(d)
d2 = loadData()
print(d2)
