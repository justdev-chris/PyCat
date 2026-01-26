import sys
import os

# Import translator
try:
    from keywords import translate
except:
    from .keywords import translate

def run():
    # No file = error
    if len(sys.argv) < 2:
        print("Error: Need filename")
        print("Use: pycat file.pycat")
        sys.exit(1)
    
    # Help
    if sys.argv[1] in ['-h', '--help']:
        print("PyCat: Run with: pycat file.pycat")
        sys.exit(0)
    
    # Run file
    try:
        with open(sys.argv[1], 'r') as f:
            code = f.read()
        
        python_code = translate(code)
        exec(python_code)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()
