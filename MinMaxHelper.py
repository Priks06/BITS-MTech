class MinMaxHelper:

    inputData = []
    typeOfData = ""

    # Clear previous contents of the output file
    def __init__(self, inputLine):
        self.inputData = inputLine

    # This function will find the type of representation of the given data
    # It can be on of the following types:
    # 1. Strictly increaing
    # 2. Strictly decreasing
    # 3. Minima
    # 4. Maxima
    def findTypeOfRepresentation(self):
        # If given input data is empty or null, return "InvalidData" string and exit
        if not self.inputData or len(self.inputData) == 0:
            return "InvalidData"
        # If only single element present, then default is increasing order
        if len(self.inputData) == 1:
            self.typeOfData = "Increasing"
        # If 2 or more elements are present then compare the orientation of the first two elements
        # and the last two elements to find the type of representation
        else:
            slope1 = self.findSlope(self.inputData[0], self.inputData[1])
            l = len(self.inputData)
            slope2 = self.findSlope(self.inputData[l-2], self.inputData[l-1])
            # If both slopes are equal then it is either increasing or decreasing order
            if slope1 == slope2:
                # If slope = 1 then increasing order else decreasing order
                self.typeOfData = self.findIncreasingOrDecreasingBySlope(slope1)
            # If first two elements are in increasing order and last two in decreasing,
            # it means the representation is maxima
            elif slope1 == 1 and slope2 == -1:
                self.typeOfData = "Maxima"
            # If first two elements are in decreasing order and last two in increasing,
            # it means the representation is minima
            elif slope1 == -1 and slope2 == 1:
                self.typeOfData = "Minima"
        return self.typeOfData

    # This function will find the minima element if the type of represenation is inc, dec or minima
    # and will find the maxima element if the type of represenation is maxima.
    def findMinimaOrMaxima(self):
        if self.typeOfData == "Increasing":
            return self.inputData[0]
        elif self.typeOfData == "Decreasing":
            return self.inputData[len(self.inputData) - 1]
        elif self.typeOfData == "Minima":
            return self.findTypeRecursively(0, len(self.inputData)-1, True)
        elif self.typeOfData == "Maxima":
            return self.findTypeRecursively(0, len(self.inputData)-1, False)

    # Find the type of representation assuming that it will
    # either be a minima function or a maxima function depending on the input parameter minimaOrMaxima
    # input: start: start index of the sub-array
    # input: end: end index of the sub-array
    # input: minimaOrMaxima: boolean flag, if true then consider minima else consider maxima
    # return: the minima or maxima element, if present,
    # will return no element if increasing or decresing graph
    def findTypeRecursively(self, start, end, minimaOrMaxima):
        # This method will be called only when the input data has 3 or more elements.
        # If 3 or more elements are present then apply modified Binary Search Tree algorithm
        # to find minima (or maxima) element
        mid = int(start + (end - start)/2)
        # If mid is lesser than both its neighbors, then it is the minima element
        if self.inputData[mid] <= self.inputData[mid-1] and self.inputData[mid] <= self.inputData[mid+1]:
            return self.inputData[mid]
        # If mid is greater than both its neighbors, then it is the maxima element
        if self.inputData[mid] >= self.inputData[mid-1] and self.inputData[mid] >= self.inputData[mid+1]:
            return self.inputData[mid]
        # If mid is greater than left neighbor and lesser than right neighbor, then it is increasing currently
        # Recursively find if there is a minima or maxima present
        if self.inputData[mid] >= self.inputData[mid-1] and self.inputData[mid] <= self.inputData[mid+1]:
            # Find minima, if present
            if minimaOrMaxima:
                # Recursively traverse the left half of the current sub-array till we reach the minima
                return self.findTypeRecursively(start, mid, minimaOrMaxima)
            # Find maxima, if present
            else:
                # Recursively traverse the right half of the current sub-array till we reach the maxima
                return self.findTypeRecursively(mid, end, minimaOrMaxima)
        # If mid is lesser than left neighbor and greater than right neighbor, then it is decreasing currently
        # Recursively find if there is a minima or maxima present
        if self.inputData[mid] <= self.inputData[mid-1] and self.inputData[mid] >= self.inputData[mid+1]:
            # Find minima, if present
            if minimaOrMaxima:
                # Recursively traverse the right half of the current sub-array till we reach the minima
                return self.findTypeRecursively(mid, end, minimaOrMaxima)
            # Find maxima, if present
            else:
                # Recursively traverse the left half of the current sub-array till we reach the maxima
                return self.findTypeRecursively(start, mid, minimaOrMaxima)

    # This function finds the slope (orientation) of the line based on 2 of its elements
    # It will commpare the two elements and find the order of those elements (inc or dec)
    # Input: element1 must come before element2 in the given data
    # Output: returns 1 when elements are in increasing order and -1 otherwise
    def findSlope(self, element1, element2):
        # If first element is lesser than second element then line is in increasing order
        if element1 <= element2:
            return 1
        else:
            return -1

    # This function will return the type of data representation (inc or dec) based on the slope
    # Input: Slope of the line (either 1 or -1)
    # Output: Returns "Increasing" if slope is 1 and "Decreasing" otherwise
    def findIncreasingOrDecreasingBySlope(self, slope):
        if slope == 1:
            return "Increasing"
        else:
            return "Decreasing"
