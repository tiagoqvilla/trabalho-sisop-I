import PCB


class System:
    def __init__(self, programs, scheduler=None):
        self.acc = 0
        self.pc = 0
        self.memory = []
        self.memory_size = 1024
        self.input_programs = programs
        # self.PCB = PCB()
        self.data_variables = {}

    def decoder(self):
        pass

    def addProgramsToMemory(self):
        for program in self.input_programs:
            for line in program.code_area:
                self.memory.append(line)
            for line in program.data_area:
                self.data_variables[line[0]] = line[1]
                self.memory.append(line)

        print(self.data_variables)

    def run(self):
        print("Iniciou a execução")
        self.addProgramsToMemory()

        while(True):
            inst = self.memory[self.pc]
            if inst[0] == "add":
                print("ADD")
                if inst[2] == 'I':
                    self.acc += int(inst[1])
                elif inst[2] == 'V':
                    self.acc += int(self.data_variables[inst[1]])
                else:
                    pass
                self.pc += 1
            elif inst[0] == "sub":
                print("SUB")
                if inst[2] == 'I':
                    self.acc -= int(inst[1])
                elif inst[2] == 'V':
                    print(type(int(self.data_variables[inst[1]])))
                    self.acc -= int(self.data_variables[inst[1]])
                else:
                    pass
                self.pc += 1
            elif inst[0] == "mult":
                if inst[2] == 'I':
                    self.acc *= int(inst[1])
                elif inst[2] == 'V':
                    self.acc *= int(self.data_variables[inst[1]])
                else:
                    pass
                self.pc += 1
            elif inst[0] == "div":
                if inst[2] == 'I':
                    self.acc /= int(inst[1])
                elif inst[2] == 'V':
                    self.acc /= int(self.data_variables[inst[1]])
                else:
                    pass
                self.pc += 1
            elif inst[0] == "load":
                print("LOAD")
                if inst[2] == 'I':
                    self.acc = int(inst[1])
                elif inst[2] == 'V':
                    self.acc = int(self.data_variables[inst[1]])
                else:
                    pass
                self.pc += 1
            elif inst[0] == "store":
                print("STORE")
                if inst[2] == 'I':
                    self.data_variables[inst[1]] = str(self.acc)
                elif inst[2] == 'V':
                    self.data_variables[inst[1]] = str(self.acc)
                else:
                    pass
                self.pc += 1
            # elif inst[0] == 'loop:' or inst[0] == 'fim:':
            #     self.pc += 1
            #     pass
            elif inst[0] == "BRANY":
                print("BRANY")
                self.pc = self.memory.index([inst[1] + ":"]) + 1
            elif inst[0] == "BRPOS":
                print("BRPOS")
                if self.acc > 0:
                    self.pc = self.memory.index([inst[1] + ":"]) + 1
                else:
                    self.pc += 1
            elif inst[0] == "BRZERO":
                print("BRZERO")
                if self.acc == 0:

                    self.pc = self.memory.index([inst[1] + ":"]) + 1
                else:
                    self.pc += 1

            elif inst[0] == "BRNEG":
                print("BRNEG")
                if self.acc < 0:
                    self.pc = self.memory.index([inst[1] + ":"]) + 1
                else:
                    self.pc += 1

            elif inst[0] == 'syscall':
                print("SYSCALL")
                if inst[1] == '0':
                    print('Programa finalizado!')
                    break

                elif inst[1] == '1':
                    print(f"Acumulador: {self.acc}")
                    self.pc += 1

                elif inst[1] == '2':
                    self.acc = int(input(">"))
                    self.pc += 1

            else:
                self.pc += 1

            print(f"Dados de memória: {self.data_variables}")
            print(f"ACC: {self.acc}")
            print(f"PC: {self.pc}")
        print(self.data_variables)
        print(self.acc)
