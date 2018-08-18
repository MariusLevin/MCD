# LIBRAIRIES
import os.path
import networkx as nx
import matplotlib.pyplot as plt
import csv

# FUNCTIONS
def saveData(dictionary):
    with open('../data/data.txt', 'w') as f:
        for key, value in dictionary.items():
            f.write('%s:%s\n' % (key, value))

def loadData():
    dictionary = {}
    with open('../data/data.txt') as r:
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

def visualizeData(dictionary):
    # Create graph
    G = nx.Graph()

    # Create nodes
    G.add_nodes_from(dictionary.keys())

    # Create edges
    for key in dictionary.keys():
        for value in dictionary[key]:
            G.add_edge(key, value, name='ok')

    # Draw graph
    nx.draw_networkx(G)
    plt.show()

def distanceCalculation(data, artist1, artist2):
    list1 = [artist1]
    list2 = []
    seen = []
    level = 1

    while (1):
        for artist in list1:
            seen.append(artist)
            sons = getSon(data, artist)
            for son in sons:
                if son == artist2:
                    return level
                elif son not in list2 and son not in seen:
                    list2.append(son)
        list1 = list2
        list2 = []
        level = level + 1

        if list1 == [] and list2 == []:
            return "No link"

def getSon(data, artist):
    return data[artist]

# WELCOME MESSAGE
print("Welcome to the Music Colaborative Distance Tool\n")

# DICTIONARY
data = {}

# LOAD OWN DATA
if os.path.isfile("../data/data.txt") == True:
    data = loadData()

# OR GET BACK SPOTIFY DATA
else:
    pass

print(data)

# SHOW NETWORK
visualizeData(data)

# DO RESEARCH
print("Calculation of the colaborative distance between to artist\n")
artist1 = input("Artist 1:")
artist2 = input("Artist 2:")

if artist1 in data.keys() and artist2 in data.keys():
    print("\n" + str(distanceCalculation(data, artist1, artist2)))
else:
    print("\nWrong artist name")
