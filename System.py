import PCB

class System:
    def __init__(self, programs, scheduler):
        self.acc = 0
        self.memory = []
        self.memory_size = 1024
        self.pc = 0
        self.PCB = PCB()
        pass
    
    def decoder(self):
        pass
    
    def run(self):
        while(1):
            pass