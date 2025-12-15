from processcore.state import ProcessState

class Process:
    def __init__(self, name: str):
        self.name = name
        self.state = ProcessState.PENDING
        self.error: str | None = None
    
    def run(self):
        self.state = ProcessState.RUNNING
        
        try:
            self.state = ProcessState.COMPLETED
        except Exception as e:
            self.state = ProcessState.FAILED
            self.error = str(e)