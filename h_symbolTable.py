"""
This class will store the symbols that the parser encounters. On first pass the parser will pass labels to the 
table as well ad resolve variable values. The second pass will resolve the values of labels referenced.
"""
class SymbolTable:

    def __init__(self):
        # first we assign the hack computers built in labels to the registers and the screen/kbd
        self.symbol_table = {"SP": "0", "LCL" : "1", "ARG" : "2" , "THIS" : "3", "THAT" : "4", "R0" : "0", "R1" : "1", "R2" : "2", "R3" : "3", "R4" : "4", "R5" : "5", "R6" : "6", "R7" : "7", "R8" : "8", "R9" : "9", "R10" : "10", "R11" : "11", "R12" : "12", "R13" : "13", "R14" : "14", "R15" : "15", "SCREEN" : "16384", "KBD" : "24576"}

    def addEntry(self, symbol, address = None):
        self.symbol_table[symbol] = address

    def contains(self, symbol):
        return symbol in self.symbol_table
    
    def getAddress(self, symbol):
        if self.contains(symbol):
            return self.symbol_table[symbol]
        else:
            raise KeyError("The symbol does not exist!")

