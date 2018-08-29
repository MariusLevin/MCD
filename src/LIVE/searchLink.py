# coding: utf-8

def getNames():
    print("Calculation of the colaborative distance between to artist\n")
    a1 = input("Artist 1: ")
    a2 = input("Artist 2: ")
    if checkArtistNameInSpotify(a1) == False:
        a1 = False
    if checkArtistNameInSpotify(a2) == False:
        a2 = False
    return a1, a2

class artist:
    # CONSTRUCTOR
    def __init__(self, name, father, album, song):
        self.name = name
        self.father = father
        self.albumFather = album
        self.songFather = song

    # OPERATORS
    def __eq__(self, artist):
        return (self.name == artist.getName())

    # METHODS


    # GETTER
    def getName(self):
        return self.name

    def getFather(self):
        return self.father

    def getAlbumFather(self):
        return self.albumFather

    def getSongFather(self):
        return self.songFather

def getAlbums(artist):
    pass

def getSongs(album):
    pass

def getCredits(song):
    pass

def checkArtistNameInSpotify(artistName):
    pass

# WELCOME MESSAGE
print("Welcome to the Music Colaborative Distance Tool\n")

# GET ARTIST NAME
a1, a2 = getNames()

# CHECK ARTIST NAME
if a1 == False or a2 == False:
    print("Artist name not in Spotify")
else:
    # CREATE FIRST ARTIST OBJECT
    artistA = artist(a1, None, None, None)
    artistB = artist(a2, None, None, None)

    # INIT
    artistSearchList = [artistA]
    artistSeen = {}
    end = None

    # BREADTH FIRST SEARCH
    while artistSearchList != []:
        for art in artistSearchList:
            if art == artistB:
                end = art
                break
            artistSeen[art.getName] = art
            albums = getAlbums(art)
            for alb in albums:
                songs = getSongs(alb)
                for song in songs:
                    credits = getCredits(song)
                    for crd in credits:
                        a = artist(crd, art, alb, song)
                        if a.getName() not in artistSeen.keys():
                            artistSearchList.append(a)

    # RESULT
    if end == None:
        print("Distance calculation not possible")
    else:
        print("Distance calculation possible \n")
        res = ""
        node = end
        while node.getFather() != None:
            res = node.getName() + "\t" + node.getAlbumFather() + "\t" + node.getSongFather() + "\n" + res
            node = node.getFather()

        res = node.getName() + "\n" + res
        print(res)
