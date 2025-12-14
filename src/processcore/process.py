class Process:
    def __init__(self, name: str):
        self.name = name
        self.state = "created"
        self.error: str | None = None
    
    def run(self):
        self.state = "running"
        
        try:
            self.state = "completed"
        except Exception as e:
            self.state = "failed"
            self.error = str(e)