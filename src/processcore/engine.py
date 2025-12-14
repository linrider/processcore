from processcore.process import Process

class Engine():
    def run(self, process: Process) -> Process:
        process.run()
        return process
        