# get number of bits in each binary number
binLength = int(input("Number of bits: "))

# data structure
class Data:
    # Inherent Data Types:
    #num The number this binary represents
    #bin the binary representation of this number
    #parents = [] the parents of this binary representation, or the nubers it came from


    # default constructor
    def __init__(self, numStr):
        try:
            self.num = int(numStr)
            self.bin = format(int(numStr), '0' + str(binLength) + 'b')
            self.parents = [self.num]
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

def combine(data1, data2):
    """This function will need to take two objects as a member and return another object that is a result of the two combined"""
    for i in range(len(data1.bin)):
        if data1.bin[i] != data2.bin[i]:
            # looks for a difference, since these can combine you know there is only one difference in the two strings
            new_string = data1.bin
            new_string = new_string[:i] + '-' + new_string[i+1:]
            new_data = Data(new_string)
    new_data.parents = data1.parents + data2.parents
    return new_data

