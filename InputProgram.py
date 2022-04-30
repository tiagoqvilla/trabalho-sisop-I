class InputProgram():
    def __init__(self, program_data, arrival_time, priority, quantum):
        self.code_area = []
        self.data_area = []
        self.program_data = program_data
        self.arrival_time = arrival_time
        self.priority = priority
        self.quantum = quantum

    def processProgramData(self):
        for element in self.program_data:
            if element != ['.endcode']:
                self.code_area.append(element)
