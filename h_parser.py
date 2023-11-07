import re

"""
The Parser class take a file path as input (the .s file) and opens a file stream. The contructor will perform an inital pass 
and remove any comment lines, white space and inline comments leaving only the actual assembly code. This will be stored in a 
list and class methods will act on this list.
"""

class Parser:

    def __init__(self, file_path):
        self.file = open(file_path, "r")
        self.commands = self._pre_parse(self.file)
        self.file.close()
        # this will index into the commands list and keep track of the current command to be parsed
        self.cmd_pntr = 0
        # this will be the command string literal
        self.current_command = self.commands[self.cmd_pntr]

    def _pre_parse(self, file_obj):
        all_lines = file_obj.readlines()
        commands = []
        for line in all_lines:
            # remove all white  space from the lines 
            line = line.replace(" ", "")
            # if the whole line is comment or just an empty line we will skip past
            if line[0] == "/" or line[0] == "\n":
                continue
            else:
                # here the split will seperate the command from any posible inline comments and discard the comments
                line = line.split("/")
                # make sure to remove the new line characters in the commands!
                commands.append(line[0].strip("\n"))
        return commands
    
    def hasMoreCommands(self):
        return not(self.cmd_pntr == (len(self.commands)) -1 )
    
    def advance(self):
        if self.hasMoreCommands():
            self.cmd_pntr += 1
            self.current_command = self.commands[self.cmd_pntr]
            return True
        return False

    # This class method returns a single character that signals the current kind of command being read. "A" for @ etc
    def commandType(self):
        if self.current_command[0] == "@":
            return "A"
        elif self.current_command[0] == "(":
            return "L"
        else:
            return "C"

    # returns the symbol (xxx) or decimal value of current command. Should only be used with command types A and L    
    def symbol(self):
        com_type = self.commandType()
        if com_type == "C":
            raise TypeError("cannot parse symbols for non-symbolic instruction type!")
        else:
            if com_type == "A":
                return self.current_command[1:]
        # if its a label command we return everything between the ()
        return self.current_command[1:-1]

    def get_command(self):
        return self.current_command
    
    # returns the destination field in a C-type instruction
    def dest(self):
        if self.commandType() != "C":
            raise TypeError("cannot parse dest field of non C-type instruction! Instruction is: " + self.commandType())
        else:
            # as dest is an optional field we check if the command has the '=' character first
            if "=" in self.current_command:
                return self.current_command.split("=")[0]
            else:
                # will return when there is no dest in the instruction
                return "null"
            
    def jump(self):
        if self.commandType() != "C":
            raise TypeError("cannot parse jump field of non C-type instruction! Instruction is: " + self.commandType())
        else:
            # jump is optional so we need to check that it has been given
            if ";" in self.current_command:
                return self.current_command.split(';')[-1]
            else:
                return "null"
            
    def comp(self):
        if self.commandType() != "C":
            raise TypeError("cannot parse comp field of non C-type instruction! Instruction is: " + self.commandType())
        else:
            # in the event we have an intruction where all fields are specified or just the dest and comp
            if ("=" in self.current_command) or ("=" in self.current_command and ";" in self.current_command):
                return re.split('[=;]', self.current_command)[1]
            else:
                return self.current_command.split(";")[0]
            
    def reset(self):
        self.cmd_pntr = 0
        self.current_command = self.commands[self.cmd_pntr]
            
if __name__ == "__main__":
    fp = "Max.asm"
    p = Parser(fp)
    while (p.hasMoreCommands()):
        if p.commandType() != "C":
            print(f"{p.get_command() : <20}" + "Command Type: " + p.commandType() + "   " + "Symbol: " + p.symbol())
        else:
            print(f"{p.get_command() : <20}" + "Command Type: " + p.commandType() + "   " + "Dest: " + f"{p.dest() : <20}" + "Comp: " + f"{p.comp() : <20}" + "Jump: " + f"{p.jump() : <20}")
        p.advance()
    if p.commandType() != "C":
        print(f"{p.get_command() : <20}" + "Command Type: " + p.commandType() + "   " + "Symbol: " + p.symbol())
    else:
        print(f"{p.get_command() : <20}" + "Command Type: " + p.commandType() + "   " + "Dest: " + f"{p.dest() : <20}" + "Comp: " + f"{p.comp() : <20}" + "Jump: " + f"{p.jump() : <20}")
    