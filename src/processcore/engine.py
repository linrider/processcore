from processcore.process import Process

class Engine():
    def run(self, process: Process) -> Process:
        return self._execute(process)
    
    def _execute(self, process: Process) -> Process:
        process.run()
        return process
        