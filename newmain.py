import os
from semantics import test, primitive, printDifficulty

# For testing purposes
# test()
# print(primitive("faranduleado"))
# print(primitive("maestras"))
# print(primitive("lloré"))
# print(primitive("paisaje"))
# print(primitive("arabilidad"))

# TODO: implement a simple cli for evaluating and comparing books
pathBooks = os.curdir + os.sep + "books" + os.sep
files = os.listdir(pathBooks)
# print(files)
for fileName in files:
    path = pathBooks + fileName
    file = open(path, "r", encoding="UTF-8")
    print(fileName)
    printDifficulty(file)
    print("")