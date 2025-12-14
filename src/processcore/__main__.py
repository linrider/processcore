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
        if result.state == "completed":
            print(f"✔ Process '{result.name}' completed successfully")
        else:
            print(f"✖ Process '{result.name}' failed: {result.error}")

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
        
if __name__ == "__main__":
    main()