import os
from semantics import test, primitive, richness

test()

def printBookRichness(bookName, bookPath):
    bookFile = open(bookPath, "r", encoding="UTF-8")
    r = richness(bookFile)
    bookFile.close()
    sinRichness = 100 * r.sintactic[0] / r.sintactic[1]
    semRichness = 100 * r.semantic[0] / r.semantic[1]
    print(bookName)
    print(f"Sintactic richness: {str(sinRichness)[:5]}% ({r.sintactic[0]} / {r.sintactic[1]})")
    print(f"Semantic richness: {str(semRichness)[:5]}% ({r.semantic[0]} / {r.semantic[1]})")
    print("")

booksPath = os.sep.join([os.curdir, "books", ""])
booksNames = os.listdir(booksPath)

for bookName in booksNames:
    bookPath = booksPath + bookName
    printBookRichness(bookName, bookPath)