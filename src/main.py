import sys
import os
import subprocess

# Import translator
try:
    from keywords import translate
except ImportError:
    from .keywords import translate

def print_help():
    """Show help message"""
    print("🐱 PyCat - Cat-themed Programming Language")
    print("=" * 40)
    print("Usage: pycat <file.pycat>")
    print("       pycat install <package>")
    print("       pycat --help")
    print("       pycat --examples")
    print("\nExamples:")
    print("  pycat hello.pycat          # Run a file")
    print("  pycat install requests     # Install package")
    print("  pycat --help               # Show this help")

def print_examples():
    """List available examples"""
    print("🐱 PyCat Examples")
    print("=" * 40)
    examples = [
        "hello.pycat     - Hello World",
        "calculator.pycat - Simple calculator", 
        "game.pycat      - Number guessing game",
        "demo.pycat      - All features showcase"
    ]
    for ex in examples:
        print(f"  {ex}")
    print("\nThese are in the 'examples/' folder")

def pycat_install(package):
    """Install packages for PyCat (like pip install)"""
    print(f"🐱 Installing {package} for PyCat...")
    
    try:
        # Use pip to install
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Installed {package}")
        print(f"\n💡 Now in PyCat:")
        print(f"  ImportCatnip {package}")
        
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {package}")
        print("Make sure pip is installed and you have internet")
    except Exception as e:
        print(f"❌ Error: {e}")

def run_file(filename):
    """Run a PyCat file"""
    if not os.path.exists(filename):
        print(f"❌ File '{filename}' not found!")
        sys.exit(1)
    
    try:
        # Read file with encoding fallback
        with open(filename, 'rb') as f:
            raw = f.read()
        
        # Try UTF-8, fallback to latin-1
        try:
            pycat_code = raw.decode('utf-8')
        except UnicodeDecodeError:
            pycat_code = raw.decode('latin-1')
        
        python_code = translate(pycat_code)
        exec(python_code)
        
    except Exception as e:
        print(f"🐾 PyCat Error: {type(e).__name__}: {e}")
        sys.exit(1)

def run():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("❌ Error: No command provided")
        print_help()
        sys.exit(1)
    
    command = sys.argv[1]
    
    # Commands
    if command in ['-h', '--help', '/?']:
        print_help()
        sys.exit(0)
    
    elif command == '--examples':
        print_examples()
        sys.exit(0)
    
    elif command == 'install':
        if len(sys.argv) < 3:
            print("❌ Error: Package name required")
            print("Usage: pycat install <package>")
            sys.exit(1)
        pycat_install(sys.argv[2])
        sys.exit(0)
    
    else:
        # Assume it's a filename
        run_file(command)

if __name__ == "__main__":
    run()
