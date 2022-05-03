class Process:
    def __init__(self, id, code_ptr, code_size, data_ptr, data_size, priority):
        self.id = id
        self.code_ptr = code_ptr
        self.code_size = code_size
        self.data_ptr = data_ptr
        self.data_size = data_size
        self.priority = priority
        self.status = "ready"
        self.time_running = 0
        self.time_life = 0
        self.time_ready = 0
        self.waiting_io = False