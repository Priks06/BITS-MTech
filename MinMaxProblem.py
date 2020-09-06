import csv
from MinMaxHelper import MinMaxHelper

class MinMaxProblem:

    inputFileName = "files/inputPS4.txt"
    outputFileName = "files/outputPS4.txt"

     # Clear previous contents of the output file
    def __init__(self):
        outputFile = open(self.outputFileName, "w")
        outputFile.write("")
        outputFile.close()

    # Read the contents of the input file and return the data in a list of lists format.
    def readInputFile(self):
        inputData = []
        try:
            # Read the file
            with open(self.inputFileName) as csvFile:
                fileReader = csv.reader(csvFile, delimiter=' ')
                lineCount = 0
                for line in fileReader:
                    if line:
                        currArray = []
                        for num in line:
                            num = num.strip()
                            if num:
                                try:
                                    currArray.append(int(num))
                                except ValueError:
                                    print("Expected integer, found: ", num)
                                    self.writeToOutputFile("Invalid data. Expected integer, found: " + str(num))
                                    return None
                        inputData.append(currArray)
                        lineCount += 1
        except:
            print("File: " + self.inputFileName + " not found.")
            self.writeToOutputFile("ERROR: Input file: " + self.inputFileName + " not found.")
        return inputData

    # Write the given message to the output file outputPS4.txt
    def writeToOutputFile(self, msg):
        outputFile = open(self.outputFileName, "a")
        outputFile.write(msg + "\n")

if __name__ == "__main__":
    minMaxProblem = MinMaxProblem()
    inputData = minMaxProblem.readInputFile()
    if inputData == None:
        print("Found invalid input data")
        minMaxProblem.writeToOutputFile("ERROR: Invalid input found")
    elif len(inputData) == 0:
        print("No input data found")
        minMaxProblem.writeToOutputFile("ERROR: No input data found")
    else:
        print("Processing")
        for inputLine in inputData:
            helper = MinMaxHelper(inputLine)
            typeOfData = helper.findTypeOfRepresentation()
            if typeOfData == "InvalidData":
                print("Invalid data found")
                minMaxProblem.writeToOutputFile("ERROR: Invalid data found")
                continue
            minOrMaxElement = helper.findMinimaOrMaxima()
            minMaxProblem.writeToOutputFile(typeOfData + " " + str(minOrMaxElement))
