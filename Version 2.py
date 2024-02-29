# simpletron computer
import math

# command definitions
SIZE = 1000
SENTINEL = -99999
TRUE = 1
FALSE = 0
READ = 10
WRITE = 11
NEWLINE = 12
LOAD = 20
STORE = 21
ADD = 30
SUBTRACT = 31
DIVIDE = 32
MULTIPLY = 33
EXPONENT = 34
MODULUS = 35
BRANCH = 40
BRANCHNEG = 41
BRANCHZERO = 42
HALT = 43

# function prototypes
def validWord(word):
    return word >= -9999 and word <= 9999

# function loads instruction
def load(loadMemory):
    instruction = 0  # current instruction
    i = 0  # indexing variable
    print("Welcome to Simpletron.")
    print("Please enter your program one data word(instruction) at a time.")
    print("I will type the location number and a question mark(?).")
    print("You then type the word for that location.")
    print("Type the sentinel -99999 to stop entering your program.\n\n\n")
    print("00 ?")
    instruction = int(input())  # read instruction
    # while sentinel is not input by user
    while instruction != SENTINEL:
        # test instruction for validity
        if not validWord(instruction):
            print("Number out of range. Please enter again.")
        else:
            loadMemory[i] = instruction
            i += 1
        print("%02d ? " % i)
        instruction = int(input())

def execute(memory, acPtr, icPtr, irPtr, opCodePtr, opPtr):
    fatal = FALSE  # fatal error flag
    temp = 0  # temporary holding space
    print("\nBEGIN SIMPLETRON EXECUTION\n\n")
    # separate operation code and operand
    irPtr[0] = memory[icPtr[0]]
    opCodePtr[0] = irPtr[0] // 100
    opPtr[0] = irPtr[0] % 100
    # loop while command is not HALT or fatal
    # ie, while we don't stop or hit an error
    while opCodePtr[0] != HALT and not fatal:
        # determine appropriate action
        if opCodePtr[0] == READ:
            print("Enter an integer: ")
            temp = int(input())
            while not validWord(temp):
                print("Number out of range. Please enter again:  ")
                temp = int(input())
            memory[opPtr[0]] = temp
            icPtr[0] += 1
        elif opCodePtr[0] == WRITE:
            print("Contents of %02d: %d\n" % (opPtr[0], memory[opPtr[0]]))
            icPtr[0] += 1
        elif opCodePtr[0] == LOAD:
            acPtr[0] = memory[opPtr[0]]
            icPtr[0] += 1
        elif opCodePtr[0] == STORE:
            memory[opPtr[0]] = acPtr[0]
            icPtr[0] += 1
        elif opCodePtr[0] == ADD:
            temp = acPtr[0] + memory[opPtr[0]]
            if not validWord(temp):
                print("FATAL ERROR:  Acuumulator overflow\n")
                print("SIMPLETRON EXECUTION ABNORMALLY TERMINATED\n")
                fatal = TRUE
            else:
                acPtr[0] = temp
                icPtr[0] += 1
        elif opCodePtr[0] == SUBTRACT:
            temp = acPtr[0] - memory[opPtr[0]]
            if not validWord(temp):
                print("FATAL ERROR:  Acuumulator overflow\n")
                print("SIMPLETRON EXECUTION ABNORMALLY TERMINATED\n")
                fatal = TRUE
            else:
                acPtr[0] = temp
                icPtr[0] += 1
        elif opCodePtr[0] == MULTIPLY:
            temp = acPtr[0] * memory[opPtr[0]]
            if not validWord(temp):
                print("FATAL ERROR:  Acuumulator overflow\n")
                print("SIMPLETRON EXECUTION ABNORMALLY TERMINATED\n")
                fatal = TRUE
            else:
                acPtr[0] = temp
                icPtr[0] += 1
        elif opCodePtr[0] == EXPONENT:
            temp = math.pow(acPtr[0], memory[opPtr[0]])
            if not validWord(temp):
                print("FATAL ERROR:  Acumulator overflow\n")
                print("SIMPLETRON EXECUTION ABNORMALLY TERMINATED\n")
                fatal = TRUE
            else:
                acPtr[0] = temp
                icPtr[0] += 1
        elif opCodePtr[0] == DIVIDE:
            if memory[opPtr[0]] == 0:
                print("FATAL ERROR: Attempted to divide by zero...\n")
                print("SIMPLETRON EXECUTION ABNORMALLY TERMINATED\n")
                fatal = TRUE
            else:
                acPtr[0] /= memory[opPtr[0]]
                icPtr[0] += 1
        elif opCodePtr[0] == MODULUS:
            if memory[opPtr[0]] == 0:
                print("FATAL ERROR: Attempted to divide by zero...\n")
                print("SIMPLETRON EXECUTION ABNORMALLY TERMINATED\n")
                fatal = TRUE
            else:
                acPtr[0] %= memory[opPtr[0]]
                icPtr[0] += 1
        elif opCodePtr[0] == BRANCH:
            icPtr[0] = opPtr[0]
        elif opCodePtr[0] == BRANCHNEG:
            if acPtr[0] < 0:
                icPtr[0] = opPtr[0]
            else:
                icPtr[0] += 1
        elif opCodePtr[0] == BRANCHZERO:
            if acPtr[0] == 0:
                icPtr[0] = opPtr[0]
            else:
                icPtr[0] += 1
        else:
            print("FATAL ERROR: invalid opcode detected..\n\n")
            print("SIMPLETRON EXECUTION ABNORMALLY TERMINATED\n\n")
            fatal = TRUE
        # separate next operation code and operand
        irPtr[0] = memory[icPtr[0]]
        opCodePtr[0] = irPtr[0] // 100
        opPtr[0] = irPtr[0] % 100
    print("\nEND SIIMPLETRON EXECUTION\n")

def dump(memory, accumulator, instructionCounter, instructionRegister, operationCode, operand):
    print("\n%s\n%-23s%+05d\n%-23s%5.2d\n%-23s%+05d\n%-23s%5.2d\n%-23s%5.2d" % ("REGISTERS:", "accumulator", accumulator, "instructioncounter",
        instructionCounter, "instructionregister", instructionRegister,  "operationcode", operationCode, "operand", operand))
    print("\n\nMEMORY:\n    ", end="")
    # print column headers
    for i in range(10):
        print("%5d " % i, end="")
    # print row headers and memory contents
    for i in range(SIZE):
        # print in increments of 10
        if i % 10 == 0:
            print("\n%2d " % i, end="")
        print("%+05d " % memory[i], end="")
    print("\n")

def main():
    memory = [0] * SIZE  # define memory array
    ac = 0  # accumulator
    ic = 0  # instruction counter
    opCode = 0  # operation code
    op = 0  # operand
    ir = 0  # instruction register
    # clear memory
    for i in range(SIZE):
        memory[i] = 0
    load(memory)
    execute(memory, [ac], [ic], [ir], [opCode], [op])
    dump(memory, ac, ic, ir, opCode, op)

main()


