
sortHeader = ""
def header(song):
    return song[sortHeader]

def displaySong(headers, song):
    string = ""
    for header in headers:
        string += song[header] + ' '
    print(string)

def displayHeader(header):
    string = ""
    for v in header:
        string += v + ' '
    print(string)

def solve():
    global sortHeader

    headers = input().split()

    songs = []
    numSongs = int(input())
    for i in range(numSongs):
        song = input().split()
        formatedSong = {}
        for j in range(len(headers)):
            formatedSong[headers[j]] = song[j]
        songs.append(formatedSong)

    numCategories = int(input())
    for i in range(numCategories):
        category = input()
        sortHeader = category
        songs.sort(key=header)
        displayHeader(headers)
        for song in songs:
            displaySong(headers, song)
        print()
solve()



