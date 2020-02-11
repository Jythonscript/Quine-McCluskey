# get number of bits in each binary number
binLength = int(input("Number of bits: "))

# data structure
class Data:

    # default constructor
    def __init__(self, num):
        self.num = num
        self.bin = format(num, '0' + str(binLength) + 'b')
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
        return str(self.num)+ " (" + self.bin  + ") "
