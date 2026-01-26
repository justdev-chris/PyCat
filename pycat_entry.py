import sys
import os

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from main import run
except ImportError:
    # Try direct import if above fails
    import importlib.util
    spec = importlib.util.spec_from_file_location("main", "src/main.py")
    main_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(main_module)
    run = main_module.run

if __name__ == "__main__":
    run()
