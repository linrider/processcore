import sys
from processcore.engine import Engine
from processcore.process import Process


def main():
    if len(sys.argv) < 2:
        print("Usage: processcore run")
        sys.exit(1)
        
    command = sys.argv[1]
    
    if command == "run":
        engine = Engine()
        process = Process(name="demo")
        result = engine.run(process)
        print(f"Process '{result.name}' finished with state: {result.state}")
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
        
if __name__ == "__main__":
    main()