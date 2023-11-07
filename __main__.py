#!/usr/bin/python3
#file pyhasm/__main__.py
from h_parser import Parser
from h_code import Code
from h_symbolTable import SymbolTable
import argparse

class Pyhasm:

    def __init__(self, source_file, target_file):
        self.sf = source_file
        self.targ = target_file
        self.p = Parser(self.sf)
        self.c = Code()
        self.s = SymbolTable()
        self.prog = []

        # first pass
        addr = 0
        while(True):
            if self.p.commandType() == "A" or self.p.commandType() == "C":
                addr += 1
            else:
                self.s.addEntry(self.p.symbol(), addr)
    
            if not self.p.advance():
                break
        
        self.p.reset()

        addr = 16
        while(True):
            if self.p.commandType() == "C":
                self.prog.append(self.c.full_instruction(self.p.dest(), self.p.comp(), self.p.jump())+"\n")
            elif self.p.commandType() == "A":
                # if the A instruction isnt symbolic, simply add it to prog
                try:
                    self.prog.append(format( int(self.p.symbol()), '016b') + "\n")
                # if the symbol is not a number then need to retrieve from the table. first check the tabel to see if it exists, otherwise add the new variable
                except:
                    if self.s.contains(self.p.symbol()):
                        self.prog.append(format( int(self.s.getAddress(self.p.symbol())), '016b') + "\n")
                    else:
                        self.s.addEntry(self.p.symbol(), addr)
                        addr += 1
                        self.prog.append(format( int(self.s.getAddress(self.p.symbol())), '016b') + "\n")
    
            if not self.p.advance():
                self.prog[-1] = self.prog[-1].strip("\n")
                break

        with open(self.targ, "w") as file:
            file.writelines(self.prog)

if __name__ == '__main__':
    parg = argparse.ArgumentParser(description="Assembler for the hack computer platform.")
    parg.add_argument("-s", required=True, type=str, help="The path to the source (.s) file.")
    parg.add_argument("-o", required=True, type=str, help="The name of the machine-code output file (will end in *.hack).")
    args = parg.parse_args()
    run = Pyhasm(args.s, args.o)