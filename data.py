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

