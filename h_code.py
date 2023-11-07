"""
This class will handle the translation of C type instruction fields into binary codes
"""
class Code:

    def __init__(self):
        # these dictionary mappings will provide the translation through the class methods. The opcode and xbits is the start of every C instruction
        self.opcode_xbits = "111"
        self.compp = {'0': '0101010', '1': '0111111', '-1': '0111010', 'D': '0001100', 'A': '0110000', '!D': '0001101', '!A': '0110001', '-D': '0001111', '-A': '0110011', 'D+1': '0011111', 'A+1': '0110111', 'D-1': '0001110', 'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011', 'A-D': '0000111', 'D&A': '0000000', 'D|A': '0010101', 'M': '1110000', '!M': '1110001', '-M': '1110011', 'M+1': '1110111', 'M-1': '1110010', 'D+M': '1000010', 'D-M': '1010011', 'M-D': '1000111', 'D&M': '1000000', 'D|M': '1010101'}
        self.destt = {"null" : "000", "M" : "001", "D" : "010", "MD" : "011", "A" : "100", "AM" : "101", "AD" : "110", "AMD" : "111"}
        self.jumpp = {"null" : "000", "JGT" : "001", "JEQ" : "010", "JGE" : "011", "JLT" : "100", "JNE" : "101", "JLE" : "110", "JMP" : "111"}

    def dest(self, dest_symbol):
        return self.destt[dest_symbol]
    
    def comp(self, comp_symbol):
        return self.compp[comp_symbol]
    
    def jump(self, jump_symbol):
        return self.jumpp[jump_symbol]
    
    def full_instruction(self, d_sym, c_sym, j_sym):
        return self.opcode_xbits + self.comp(c_sym) + self.dest(d_sym) + self.jump(j_sym)