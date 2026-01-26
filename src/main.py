# pycat_interpreter.py - Complete Implementation
import re
import sys
import math
import random
from datetime import datetime

class PyCatInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.cat_classes = {}
        
        # Built-in cat constants
        self.variables.update({
            'Mew': False,
            'Catnap': None,
            'Pawsitive': True,
            'NineLives': 9,
            'CatPi': 3.14159,
            'EmptyFoodBowl': '',
            'NoMice': [],
            'NoCatnip': {}
        })
        
        # Translation dictionaries
        self.keywords = {
            # Control flow
            'IfHungry': 'if',
            'ElseIf': 'elif',
            'Otherwise': 'else',
            'ForPrey': 'for',
            'WhileChasing': 'while',
            'Defur': 'def',
            'Fetch': 'return',
            'TryToCatch': 'try',
            'ExceptCat': 'except',
            'FinallyNap': 'finally',
            'CatCall': 'raise',
            'Scratch': 'break',
            'KeepGoing': 'continue',
            'Paws': 'pass',
            'WithWhiskers': 'with',
            'ImportCatnip': 'import',
            'FromCatTree': 'from',
            'CatClass': 'class',
            
            # Logic
            'AndCat': 'and',
            'OrCat': 'or',
            'NotCat': 'not',
            'IsCat': 'is',
            'IsNotCat': 'is not',
            'InLitterbox': 'in',
            'NotInBox': 'not in',
            
            # Assignment
            'CatGets': '=',
            'PlusGets': '+=',
            'MinusGets': '-=',
            'TimesGets': '*=',
            'DivideGets': '/=',
            'FloorGets': '//=',
            'ModGets': '%=',
            'PowerGets': '**=',
            'WalrusCat': ':=',
            
            # Special
            'AwaitTreat': 'await',
            'AsyncPounce': 'async',
            'AssertCat': 'assert',
            'DeleteMouse': 'del',
            'Unleash': 'global',
            'Purrivate': 'nonlocal',
            'LambdaCat': 'lambda',
            'Yowl': 'yield'
        }
        
        self.builtins = {
            # Basics
            'Meow': self.cat_print,
            'Beg': input,
            'CountWhiskers': len,
            'CatType': type,
            'CatID': id,
            'HelpCat': help,
            'ListToys': dir,
            
            # Type conversion
            'ToCatYears': int,
            'ToFloatCat': float,
            'CatSpeak': str,
            'IsAwake': bool,
            'CatList': list,
            'CatTangle': tuple,
            'CatDiary': dict,
            'CatCollection': set,
            'CatBytes': bytes,
            'CatterArray': bytearray,
            'ComplexCat': complex,
            
            # Math
            'CatAbs': abs,
            'CatSum': sum,
            'SmallestCat': min,
            'BiggestCat': max,
            'CatPower': pow,
            'RoundCat': round,
            'ShareTreats': divmod,
            'BinCat': bin,
            'OctoCat': oct,
            'HexCat': hex,
            'CatChar': chr,
            'CatOrder': ord,
            'CatHash': hash,
            'EnumerateMice': enumerate,
            
            # Iterables
            'CatRange': range,
            'ZipCats': zip,
            'MapCat': map,
            'FilterCat': filter,
            'SortedCats': sorted,
            'ReverseCat': reversed,
            'CatIterator': iter,
            'NextToy': next,
            'CatSlice': slice,
            'AnyCat': any,
            'AllCats': all,
            'IsCatInstance': isinstance,
            
            # Objects
            'GetCatTrait': getattr,
            'SetCatTrait': setattr,
            'HasCatTrait': hasattr,
            'RemoveTrait': delattr,
            'CatProperty': property,
            'StaticCat': staticmethod,
            'ClassyCat': classmethod,
            'SuperCat': super,
            
            # Execution
            'CatEval': eval,
            'CatExec': exec,
            'CompileCat': compile,
            'OpenCatDoor': open,
            'CatMemory': memoryview,
            'LocalCats': locals,
            'GlobalCats': globals,
            'CatVars': vars,
            'CallableCat': callable,
            
            # Misc
            'CatRepr': repr,
            'CatFormat': format,
            'BreakTime': breakpoint,
            'FetchCatnip': __import__,
            'AsyncIterCat': aiter if hasattr(__builtins__, 'aiter') else None,
            'AsyncNextCat': anext if hasattr(__builtins__, 'anext') else None,
            
            # Cat-specific functions
            'Purr': lambda x: print(f"😺 {x}"),
            'Hiss': lambda x: print(f"😾 {x}"),
            'CatNap': lambda x: print(f"😴 {x}"),
            'Pounce': print,
            'ChaseMouse': lambda: random.choice(['🐭', '🧀', '🎣']),
            'RandomCat': lambda: random.choice(['😸', '😹', '😺', '😻', '😼', '😽', '😾', '😿', '🙀']),
            'CatNow': datetime.now,
            'CatMath': math,
            'CatRandom': random
        }
        
        self.operators = {
            'PlusCat': '+',
            'MinusCat': '-',
            'TimesCat': '*',
            'DivideCat': '/',
            'FloorCat': '//',
            'ModCat': '%',
            'PowerCat': '**',
            'SameAs': '==',
            'NotSame': '!=',
            'BiggerCat': '>',
            'SmallerCat': '<',
            'BiggerOrEqual': '>=',
            'SmallerOrEqual': '<='
        }
    
    def cat_print(self, *args, **kwargs):
        """Special Meow function with cat emoji"""
        if args:
            print("🐱", *args, **kwargs)
        else:
            print("🐱", end='', **kwargs)
    
    def translate_line(self, line):
        """Convert PyCat to Python line by line"""
        original = line
        
        # Replace operators first
        for pycat_op, python_op in self.operators.items():
            line = line.replace(pycat_op, python_op)
        
        # Replace assignment operators
        for pycat_assign, python_assign in {k:v for k,v in self.keywords.items() if k.endswith('Gets') or k == 'WalrusCat'}.items():
            line = line.replace(pycat_assign, python_assign)
        
        # Replace keywords (carefully to avoid partial replacements)
        words = line.split()
        for i, word in enumerate(words):
            # Check for keywords at word boundaries
            if word in self.keywords and not (word.endswith('(') or word.endswith(')') or word.endswith(':') or word.endswith(',')):
                words[i] = self.keywords[word]
        
        line = ' '.join(words)
        
        # Replace built-in functions (more careful replacement)
        for pycat_func, _ in self.builtins.items():
            # Replace function calls like Meow( -> print(
            pattern = r'\b' + re.escape(pycat_func) + r'\('
            line = re.sub(pattern, self.keywords.get(pycat_func, pycat_func.lower()) + '(', line)
            
            # Replace standalone function names
            pattern = r'\b' + re.escape(pycat_func) + r'\b'
            if pycat_func in self.keywords:
                line = re.sub(pattern, self.keywords[pycat_func], line)
            else:
                line = re.sub(pattern, pycat_func.lower(), line)
        
        # Special handling for cat emotes in strings
        if 'Purr(' in original or 'Hiss(' in original:
            line = line.replace('print(', 'print("😺 " + str(').replace('))', ')')
        
        return line
    
    def preprocess(self, code):
        """Handle multi-line constructs before translation"""
        lines = code.split('\n')
        processed = []
        in_multiline = False
        multiline_content = []
        
        for line in lines:
            stripped = line.strip()
            
            # Skip comments
            if stripped.startswith('#'):
                processed.append(line)
                continue
            
            # Handle multi-line strings
            if '"""' in line or "'''" in line:
                if not in_multiline:
                    in_multiline = True
                    multiline_content = [line]
                else:
                    multiline_content.append(line)
                    in_multiline = False
                    processed.append('\n'.join(multiline_content))
                continue
            
            if in_multiline:
                multiline_content.append(line)
                continue
            
            # Handle indentation
            indent = len(line) - len(line.lstrip())
            indent_str = ' ' * (indent // 4) if indent % 4 == 0 else ' ' * indent
            
            # Translate the actual code
            if stripped:
                translated = self.translate_line(stripped)
                processed.append(indent_str + translated)
            else:
                processed.append('')
        
        return '\n'.join(processed)
    
    def execute(self, code, filename="<pycat>"):
        """Execute PyCat code"""
        try:
            # Preprocess and translate
            python_code = self.preprocess(code)
            
            # Add builtins to execution context
            exec_globals = {
                '__name__': '__main__',
                '__file__': filename,
                '__builtins__': __builtins__,
            }
            
            # Add all our built-in functions
            exec_globals.update(self.builtins)
            exec_globals.update(self.variables)
            
            # Execute the translated Python code
            exec(python_code, exec_globals, self.variables)
            
        except SyntaxError as e:
            print(f"🐾 PyCat Syntax Error: {e}")
            print(f"   in: {e.text}")
        except Exception as e:
            print(f"🐾 PyCat Error: {type(e).__name__}: {e}")
    
    def run_file(self, filename):
        """Run a .pycat file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                code = f.read()
            
            print(f"🐈 Running {filename}...")
            print("=" * 40)
            self.execute(code, filename)
            
        except FileNotFoundError:
            print(f"🐾 Error: File '{filename}' not found!")
    
    def repl(self):
        """Read-Eval-Purr Loop"""
        print("🐈 Welcome to PyCat REPL!")
        print("Type 'exit' or 'quit' to leave")
        print("Type 'help' for help")
        print("=" * 40)
        
        while True:
            try:
                # Get input with cat prompt
                line = input("😸 pycat> ").strip()
                
                if line.lower() in ['exit', 'quit', 'bye']:
                    print("🐾 Goodbye! Meow!")
                    break
                elif line.lower() == 'help':
                    self.show_help()
                    continue
                elif line.lower() == 'vars':
                    self.show_variables()
                    continue
                elif line.lower().startswith('cat '):
                    self.cat_command(line[4:])
                    continue
                
                # Special REPL-only: if line starts with variable assignment
                # and no colon, add implicit print for expressions
                if not any(line.startswith(kw) for kw in ['Defur', 'CatClass', 'IfHungry', 'ForPrey', 'WhileChasing']) and ':' not in line:
                    if 'CatGets' in line:
                        # It's an assignment
                        self.execute(line)
                    else:
                        # It's an expression, print the result
                        translated = self.translate_line(line)
                        result = eval(translated, {**self.builtins, **self.variables})
                        if result is not None:
                            print(f"🐱 {result}")
                else:
                    self.execute(line)
                    
            except KeyboardInterrupt:
                print("\n🐾 Interrupted!")
                break
            except Exception as e:
                print(f"🐾 Error: {type(e).__name__}: {e}")
    
    def show_help(self):
        """Show help message"""
        print("\n🐈 PyCat Help:")
        print("-" * 30)
        print("BASIC COMMANDS:")
        print("  exit/quit    - Leave PyCat")
        print("  vars         - Show variables")
        print("  cat <cmd>    - Cat commands")
        print("  help         - This message")
        print("\nQUICK EXAMPLES:")
        print("  Meow('Hello!')")
        print("  x CatGets 5")
        print("  Meow(x PlusCat 3)")
        print("  IfHungry x > 3: Meow('Big!')")
    
    def show_variables(self):
        """Show all defined variables"""
        print("\n📦 Variables:")
        for name, value in self.variables.items():
            if not name.startswith('_'):
                print(f"  {name} = {repr(value)}")
    
    def cat_command(self, cmd):
        """Special cat commands"""
        cmd = cmd.strip().lower()
        
        if cmd == 'nap':
            print("😴 Zzz... (sleeping for 1 second)")
            import time
            time.sleep(1)
        elif cmd == 'play':
            print("🎾 *chases ball*")
        elif cmd == 'feed':
            print("🍗 *nom nom nom*")
        elif cmd == 'stats':
            print(f"📊 Variables: {len(self.variables)}")
            print(f"📊 Functions: {len(self.functions)}")
        else:
            print(f"🐱 *{cmd}* ...meow?")

# Example PyCat programs
EXAMPLE_PROGRAMS = {
    'hello': """
# Hello World in PyCat
Meow("Hello from PyCat! 🐱")
Purr("This is a happy message!")
Hiss("Watch out for hairballs!")
""",

    'calc': """
# Calculator
x CatGets ToCatYears(Beg("Enter first number: "))
y CatGets ToFloatCat(Beg("Enter second number: "))

Meow(f"{x} PlusCat {y} = {x PlusCat y}")
Meow(f"{x} MinusCat {y} = {x MinusCat y}")
Meow(f"{x} TimesCat {y} = {x TimesCat y}")

IfHungry y NotSame 0:
    Meow(f"{x} DivideCat {y} = {x DivideCat y}")
Otherwise:
    Hiss("Cannot divide by zero!")
""",

    'loop': """
# Loop example
Meow("Counting mice...")

ForPrey i InLitterbox CatRange(1, 6):
    IfHungry i SameAs 3:
        Meow(f"🐭 Found mouse #{i}!")
        Scratch
    Otherwise:
        Meow(f"Looking... {i}")
""",

    'func': """
# Function example
Defur cat_math(a, b):
    sum CatGets a PlusCat b
    product CatGets a TimesCat b
    Fetch sum, product

result1, result2 CatGets cat_math(3, 4)
Meow(f"Sum: {result1}")
Meow(f"Product: {result2}")
""",

    'game': """
# Guess the number game
secret CatGets CatRandom().randint(1, 10)
attempts CatGets 0

Meow("Guess my number (1-10)!")

WhileChasing Pawsitive:
    guess CatGets ToCatYears(Beg("Your guess: "))
    attempts PlusGets 1
    
    IfHungry guess SmallerCat secret:
        Meow("Too small!")
    ElseIf guess BiggerCat secret:
        Meow("Too big!")
    Otherwise:
        Meow(f"🎉 Correct! It took {attempts} tries.")
        Scratch
"""
}

def main():
    """Main entry point"""
    interpreter = PyCatInterpreter()
    
    if len(sys.argv) > 1:
        # Run a file
        if sys.argv[1].endswith('.pycat'):
            interpreter.run_file(sys.argv[1])
        elif sys.argv[1] in EXAMPLE_PROGRAMS:
            print(f"🐈 Running example: {sys.argv[1]}")
            print("=" * 40)
            interpreter.execute(EXAMPLE_PROGRAMS[sys.argv[1]])
        elif sys.argv[1] == '--examples':
            print("Available examples:")
            for name in EXAMPLE_PROGRAMS:
                print(f"  {name}")
        else:
            print(f"Usage: python {sys.argv[0]} [filename.pycat]")
            print(f"       python {sys.argv[0]} [example_name]")
            print(f"       python {sys.argv[0]} --examples")
            print(f"       python {sys.argv[0]} (for REPL)")
    else:
        # Start REPL
        interpreter.repl()

if __name__ == "__main__":
    main()
