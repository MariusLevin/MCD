# FUNCTIONS
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

# TESTS
data = {'a1': ['a2'], 'a2': ['a1', 'a3', 'a4'], 'a3': ['a2'], 'a4': ['a2'], 'a5': []}

print(distanceCalculation(data, 'a1', 'a2'))
print(distanceCalculation(data, 'a1', 'a3'))
print(distanceCalculation(data, 'a1', 'a4'))
print(distanceCalculation(data, 'a1', 'a5'))