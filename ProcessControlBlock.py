from Process import Process
from InputProgram import InputProgram

class ProcessControlBlock:
    def __init__(self):
        self.running = None
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
        self.addQueueReady(process)


    def schdRoundRobin(self):
        pass

    def schdPriorityNoPreemption(self):
        # TODO retornar o id/processo que será rodado
        pass

    def schdPriorityWithPreemption(self):
        pass
    
    def addQueueReady(self, process):
        self.queue_ready.append(process)
        process.status = "ready"
    
    def addQueueBlocked(self, process):
        self.queue_blocked.append(process)
        process.status = "blocked"
        
    def addQueueFinished(self, process):
        self.queue_finished.append(process)
        process.status = "finished"
        
    def rmvQueueReady(self, process):
        self.queue_ready.remove(process)
    
    def rmvQueueBlocked(self, process):
        self.queue_blocked.remove(process)
    
    def setRunning(self, process):
        self.running_id = process
        process.status = "running"