import sys
import os
from .keywords import translate

def run():
    """Main entry point - runs PyCat code"""
    if len(sys.argv) < 2:
        print("Usage: pycat <filename.pycat>")
        print("       pycat --help")
        return
    
    if sys.argv[1] in ['-h', '--help']:
        print("PyCat - Cat-themed language")
        print("Usage: pycat filename.pycat")
        print("       pycat --help")
        return
    
    filename = sys.argv[1]
    
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found")
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        pycat_code = f.read()
    
    try:
        python_code = translate(pycat_code)
        exec(python_code)
    except Exception as e:
        print(f"PyCat Error: {type(e).__name__}: {e}")

if __name__ == "__main__":
    run()
