class Process:
    def __init__(self, name: str):
        self.name = name
        self.state = "created"
    
    def run(self):
        self.state = "completed"