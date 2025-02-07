originalBook = [
    "C4e3F6e6F5g6E7c5",
    "C4e3F6e6F5g6",
    "C4e3F6e6F5c5F4g6F7g5",
    "C4e3F6e6F5c5F4g6F7d3",
    "C4e3F6e6F5c5F4g6F7",
    "C4e3F6e6F5c5F4g5G4f3C6d3D6b3C3b4E2b6",
    "C4e3F6e6F5c5F4g5G4f3C6d3D6",
    "C4e3F6e6F5c5D6",
    "C4e3F6e6F5c5D3",
    "C4e3F6e6F5c5C3g5",
    "C4e3F6e6F5c5C3c6D6",
    "C4e3F6e6F5c5C3c6D3d2E2b3C1c2B4a3A5b5A6a4A2",
    "C4e3F6e6F5c5C3c6",
    "C4e3F6e6F5c5C3b4D6c6B5a6B6c7",
    "C4e3F6e6F5c5C3b4",
    "C4e3F6e6F5c5C3",
    "C4e3F6e6F5",
    "C4e3F6b4",
    "C4e3F5e6F4c5D6c6F7g5G6",
    "C4e3F5e6F4c5D6c6F7f3",
    "C4e3F5e6F4",
    "C4e3F5e6D3",
    "C4e3F5b4F3f4E2e6G5f6D6c6",
    "C4e3F5b4F3",
    "C4e3F5b4",
    "C4e3F4c5E6",
    "C4e3F4c5D6f3E6c6",
    "C4e3F4c5D6f3E6c3D3e2D2",
    "C4e3F4c5D6f3E6c3D3e2B6f5G5f6",
    "C4e3F4c5D6f3E6c3D3e2B6f5G5",
    "C4e3F4c5D6f3E6c3D3e2B6f5B4f6G5d7",
    "C4e3F4c5D6f3E6c3D3e2B6f5",
    "C4e3F4c5D6f3E6c3D3e2B5f5B4f6C2e7D2c7",
    "C4e3F4c5D6f3E6c3D3e2B5f5B3",
    "C4e3F4c5D6f3E6c3D3e2B5f5",
    "C4e3F4c5D6f3E6c3D3e2B5",
    "C4e3F4c5D6f3E6c3D3e2",
    "C4e3F4c5D6f3E2",
    "C4e3F4c5D6f3D3c3",
    "C4e3F4c5D6f3D3",
    "C4e3F4c5D6f3C6",
    "C4e3F4c5D6e6",
    "C4e3",
    "C4c5",
    "C4c3F5c5",
    "C4c3E6c5",
    "C4c3D3c5F6f5",
    "C4c3D3c5F6e3C6f5F4g5",
    "C4c3D3c5F6e2C6",
    "C4c3D3c5F6",
    "C4c3D3c5D6f4F5e6F6",
    "C4c3D3c5D6f4F5e6C6d7",
    "C4c3D3c5D6f4F5d2G4d7",
    "C4c3D3c5D6f4F5d2B5",
    "C4c3D3c5D6f4F5d2",
    "C4c3D3c5D6f4F5",
    "C4c3D3c5D6f4B4e3B3",
    "C4c3D3c5D6f4B4c6B5b3B6e3C2a4A5a6D2",
    "C4c3D3c5D6f4B4b6B5c6F5",
    "C4c3D3c5D6f4B4b6B5c6B3",
    "C4c3D3c5D6f4B4",
    "C4c3D3c5D6e3",
    "C4c3D3c5D6",
    "C4c3D3c5B6e3",
    "C4c3D3c5B6c6B5",
    "C4c3D3c5B6",
    "C4c3D3c5B5",
    "C4c3D3c5B4e3",
    "C4c3D3c5B4d2E2",
    "C4c3D3c5B4d2D6",
    "C4c3D3c5B4d2C2f4D6c6F5e6F7",
    "C4c3D3c5B4",
    "C4c3D3c5B3f4B5b4C6d6F5",
    "C4c3D3c5B3f3",
    "C4c3D3c5B3",
    "C4c3D3c5B2",
    "C4c3"
]
newBook = []


def translate(cell):
    letter = cell[0].lower()
    x = None
    if letter == 'a':
        x = 1
    elif letter == 'b':
        x = 2
    elif letter == 'c':
        x = 3
    elif letter == 'd':
        x = 4
    elif letter == 'e':
        x = 5
    elif letter == 'f':
        x = 6
    elif letter == 'g':
        x = 7
    elif letter == 'h':
        x = 8
    x = x - 1
    y = int(cell[1]) - 1
    return x, y


def toSize10(pos):
    return pos[0] + 1, pos[1] + 1


def flipVerticaly(pos):
    size = 10
    return abs(size - 1 - pos[0]), pos[1]


def generateCorrespondingBook():
    for l in originalBook:
        new_l = []
        for i in range(0, len(l), 2):
            pos = translate(l[i:i + 2])
            pos = toSize10(pos)
            pos = flipVerticaly(pos)
            new_l.append(pos)
        newBook.append(new_l)


generateCorrespondingBook()
print(newBook)
