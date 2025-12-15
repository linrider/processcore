import subprocess
import sys

def run_processcore(*args):
    return subprocess.run(
        [sys.executable, "-m", "processcore", *args],
        capture_output=True,
        text=True,
    )
    
def test_run_success():
    result = run_processcore("run")
    
    assert result.returncode == 0
    assert "completed successfully" in result.stdout
    
def test_unknown_command():
    result = run_processcore("unknown")
    
    assert result.returncode == 1
    assert "Unknown command" in result.stdout
    
def test_no_arguments():
    result = run_processcore()
    
    assert result.returncode == 1
    assert "Usage:" in result.stdout