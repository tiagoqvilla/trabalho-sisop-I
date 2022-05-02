class InputProgram():
    def __init__(self, name, program_data, arrival_time, priority, quantum):
        self.name = name
        self.code_area = []
        self.data_area = []
        self.program_data = program_data
        self.arrival_time = arrival_time
        self.priority = priority
        self.quantum = quantum

    def processProgramData(self):
        self.code_area = self.program_data[self.program_data.index(
            ['.code']) + 1: self.program_data.index(['.endcode'])]
        self.data_area = self.program_data[self.program_data.index(
            ['.data']) + 1: self.program_data.index(['.enddata'])]
        self.processCodeArea()

    def processCodeArea(self):
        for instr in self.code_area:
            if len(instr) < 2:
                continue
            elif '#' in instr[1]:  # Instrução com valor imediato
                instr[1] = instr[1].strip("#")
                instr.append("I")
            elif instr[0] in ["BRANY", "BRPOS", "BRZERO", "BRNEG"]:  # Instrução de branch
                instr.append("B")
            elif instr[0] == "syscall":  # Chamada de sistema
                instr.append("S")
            else:  # Instrução com valor definido em uma variável
                instr.append("V")
