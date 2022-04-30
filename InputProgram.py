class InputProgram():
    def __init__(self, program_data, arrival_time, priority, quantum):
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
