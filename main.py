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

# print the nested items in a list containing lists of Data objects
def printBigList(bigList):
    print("[", end="")
    for i in range(0, len(bigList)):
        l = bigList[i]
        print("[", end="")
        for j in range(0, len(l)):
            print(l[j].bin, end="")
            if j != len(l) - 1:
                print(",", end="")
        print("]", end="")
        if i != len(bigList) - 1:
            print(", ", end="")
    print("]")

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

# make nested list
bigList = [[]]

for i in range(0, binLength):
    bigList.append([])

for i in range(0, len(myList)):
    index = myList[i].numOnes()
    bigList[index].append(myList[i])

print("Entire list:")
printBigList(bigList)
print("")

# iterate through every pair in adjacent lists of bigList
for i in range(0, len(bigList) - 1):
    for j in range(0, len(bigList[i])):
        for k in range(0, len(bigList[i+1])):
            # data objects to compare
            #print("i = " + str(i) + ", j = " + str(j) + ", k = " + str(k))
            data1 = bigList[i][j]
            data2 = bigList[i + 1][k]
            # check if they can be combined
            if canCombine(data1, data2):
                print(data1.bin + " and " + data2.bin + " can be combined")
