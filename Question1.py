class Calculator:

    # Constructor that initializes the attributes
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.OverallResult = 0

    #Adding 2 numbers and printing the 2dp of the result
    def adder(self):
        self.OverallResult = self.input1 + self.input2
        print("Add values: {} and {} to get {:.2f}".format(self.input1, self.input2, self.OverallResult))

    #Subtracting 2 numbers and printing the 2dp of the result
    def subtractor(self):
        self.OverallResult = self.input1 - self.input2
        print("Subtract values: {} and {} to get {:.2f}".format(self.input1, self.input2, self.OverallResult))

    #Multiplying 2 numbers and printing the 2dp of the result
    def multiplier(self):
        self.OverallResult = self.input1 * self.input2
        print("Multiply values: {} and {} to get {:.2f}".format(self.input1, self.input2, self.OverallResult))

    #Dividing 2 numbers and printing the 2dp of the result
    # If second input is 0 (Divisor), then print an error message
    def divider(self):
        if self.input2 == 0:
            print("Cannot be divided by 0")
        else:
            self.OverallResult = self.input1 / self.input2
            print("Dividing: {} and {} to get {:.2f}".format(self.input1, self.input2, self.OverallResult))

    # Clears the attributes to 0
    def clear(self):
        self.input1 = 0
        self.input2 = 0
        self.OverallResult = 0
        print("All values have been reset to 0")

# Ask user for 2 numbers
input1 = float(input("Please enter the first number to be calculated: "))
input2 = float(input("Please enter the second number to be calculated: "))
# Create Calculator object
Calculator = Calculator(input1, input2)
# Call the functions defined in the class
Calculator.adder()
Calculator.subtractor()
Calculator.multiplier()
Calculator.divider()
Calculator.clear()