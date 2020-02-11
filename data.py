# get number of bits in each binary number
binLength = int(input("Number of bits: "))

# data structure
class Data:

    # default constructor
    def __init__(self, numStr):
        try:
            self.num = int(numStr)
            self.bin = format(int(numStr), '0' + str(binLength) + 'b')
        except ValueError:
            self.num = -1
            self.bin = numStr
        self.parents = []

    # return the number of "1" digits in the binary representation of the number
    def numOnes(self):
        numOnes = 0
        for digit in self.bin:
            if digit == "1":
                numOnes += 1
        return numOnes
    
    # return printable string with all of the data
    def toString(self):
        output = ""
        if self.num != -1:
            output += str(self.num)
        else:
            output += " "

        output += " (" + self.bin  + ") "
        return output


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
