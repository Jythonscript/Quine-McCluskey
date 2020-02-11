#!/usr/bin/env python3

# WARNING: importing data asks for length of binary through input()
from data import *

"""
Get base-10 numbers as user input, then put them into a list of Data objects called "myList"


to get the base-10 number from a Data object, use objectName.num

to get the binary form of the number as a string, use objectName.bin
    the bin property can be indexed like a list, so you can do something like
    if objectName.bin[0] == "1":
"""

# check if two data objects can be combined
def canCombine(data1, data2):
    # make sure that dashes are in the same spots in both
    for i in range(0, len(data1.bin)):
        if (data1.bin[i] == "-") != (data2.bin[i] == "-"):
            return False

    # check for number of ones
    diffOnes = abs(data1.numOnes() - data2.numOnes())
    if diffOnes == 1:
        # check for only one different character
        diffs = 0
        for i in range(0, len(data1.bin)):
            if data1.bin[i] != data2.bin[i]:
                diffs += 1
            if diffs > 1:
                return False
        return True
    else:
        return False

print("\nEnter numbers below (press enter when done)")

# list of Data objects
myList = []
i = 0
while True:
    # get user input
    myStr = input("Index " + str(i) + ": ")
    if myStr == "":
        break
    else:
        data = Data(myStr)
        myList.append(data)
    i += 1

# print the list
print("\nThe list:")
for data in myList:
    print(data.toString())

print("")

# iterate through every unique pair
for i in range(0, len(myList)):
    for j in range(i, len(myList)):
        # check if they can be combined
        if i != j and canCombine(myList[i], myList[j]):
            print(myList[i].bin + " and " + myList[j].bin + " can be combined")
