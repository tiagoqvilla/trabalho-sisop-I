from ProcessControlBlock import ProcessControlBlock as PCB

class System:

    def __init__(self, programs, scheduler=None):
        self.acc = 0
        self.pc = 0
        self.system_memory = []
        self.system_memory_size = 20
        self.memory = []
        self.memory_size = 1024
        self.input_programs = programs
        self.data_variables = {}
        self.memory_address_table = {}
        self.system_time = 0
        self.PCB = PCB()
    

    def addProgramsToMemory(self):
        for program in self.input_programs:
            program_address = []
            
            program_address.append(len(self.memory))
            
            for line in program.code_area:
                self.memory.append(line)
                
            program_address.append(len(program.code_area))
            program_address.append(len(self.memory))
            
            for line in program.data_area:
                self.data_variables[line[0]] = line[1]
                self.memory.append(line)
                
            program_address.append(len(program.data_area))
            
            self.memory_address_table[program] = program_address

        print(self.data_variables)
        print(self.memory_address_table)

    def initProgramProcess(self,program):
        self.PCB.createProcess(program, self.memory_address_table[program])

    def checkNewArrival(self, program):
        if program.arrival_time == self.system_time:
            #print(f"ARRIVAL TIME IGUAL AO DO SISTEMA\nAT {program.arrival_time} == ST {self.system_time}")
            return True
        else:
            #print(f"ARRIVAL TIME DIFERENTE DO SISTEMA\nAT {program.arrival_time} != ST {self.system_time}")
            return False
    
    def run(self):
        print("Iniciou a execução")
        self.addProgramsToMemory()
        
        # TODO adicionar aqui retorno do processo escalonado    
        
        while(True):
            
            # Criação de Processo no timing \/
            for program in self.input_programs:
                if self.checkNewArrival(program) == True:
                    self.initProgramProcess(program)
                    input(f"Novo processo criado:\nprograma: {program.name}\nsystem time: {self.system_time}\n> ")
                else:
                    continue
            
            # Fetch da instrução \/
            #inst = self.memory[pcb.running.contexto[0]]
            inst = self.memory[self.pc]
            
            # Decodificação da Instrução
            if inst[0] == "add":
                print("ADD")
                if inst[2] == 'I':
                    self.acc += int(float(inst[1]))
                elif inst[2] == 'V':
                    self.acc += int(float(self.data_variables[inst[1]]))
                else:
                    pass
                self.pc += 1
            
            elif inst[0] == "sub":
                print("SUB")
                if inst[2] == 'I':
                    self.acc -= int(float(inst[1]))
                elif inst[2] == 'V':
                    print(type(float(self.data_variables[inst[1]])))
                    self.acc -= int(float(self.data_variables[inst[1]]))
                else:
                    pass
                self.pc += 1
            
            elif inst[0] == "mult":
                if inst[2] == 'I':
                    self.acc *= int(float(inst[1]))
                elif inst[2] == 'V':
                    self.acc *= int(float(self.data_variables[inst[1]]))
                else:
                    pass
                self.pc += 1
            
            elif inst[0] == "div":
                if inst[2] == 'I':
                    self.acc /= int(float(inst[1]))
                elif inst[2] == 'V':
                    self.acc /= int(float(self.data_variables[inst[1]]))
                else:
                    pass
                self.pc += 1
            
            elif inst[0] == "load":
                print("LOAD")
                if inst[2] == 'I':
                    self.acc = int(float(inst[1]))
                elif inst[2] == 'V':
                    self.acc = int(float(self.data_variables[inst[1]]))
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
                    self.acc = float(input(">"))
                    self.pc += 1

            else:
                self.pc += 1

            print(f"Dados de memória: {self.data_variables}")
            print(f"ACC: {self.acc}")
            print(f"PC: {self.pc}")

            self.system_time += 1

        print(self.data_variables)
        print(self.acc)
        print(f"MEMORY: {self.memory}")
        print(f"MEMORY VAR TABLE: {self.memory_address_table}")
