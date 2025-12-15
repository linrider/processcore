import sys
from processcore.engine import Engine
from processcore.process import Process
from processcore.state import ProcessState


def main():
    if len(sys.argv) < 2:
        print("Usage: processcore run")
        return 1
        
    command = sys.argv[1]
    
    if command == "run":
        engine = Engine()
        process = Process(name="demo")
        result = engine.run(process)
        if result.state == ProcessState.COMPLETED:
            print(f"✔ Process '{result.name}' completed successfully")
            return 0
        else:
            print(f"✖ Process '{result.name}' failed: {result.error}")
            return 1

    else:
        print(f"Unknown command: {command}")
        return 1
        
if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(2)