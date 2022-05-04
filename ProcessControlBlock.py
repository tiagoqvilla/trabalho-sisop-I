from Process import Process
from InputProgram import InputProgram

class ProcessControlBlock:
    def __init__(self):
        self.running_id = 0
        self.scheduler = 0
        self.queue_ready = []
        self.queue_blocked = []
        self.queue_finished = []
        self.process_list = []


    def createProcess(self, program, memory_address_list):
        id = len(self.process_list)
        code_ptr = memory_address_list[0]
        code_size = memory_address_list[1]
        data_ptr = memory_address_list[2]
        data_size = memory_address_list[3]
        priority = program.priority

        process = Process(id, code_ptr, code_size, data_ptr, data_size, priority)

        self.process_list.append(process)
        self.queue_ready.append(process)


    def schdRoundRobin(self):
        pass

    def schdPriorityNoPreemption(self):
        # TODO retornar o id/processo que será rodado
        pass

    def schdPriorityWithPreemption(self):
        pass
    
    