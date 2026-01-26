# COMPLETE PyCat translations
CAT_TO_PYTHON = {
    # === BASIC KEYWORDS ===
    'IfHungry': 'if',
    'Otherwise': 'else', 
    'ElseIf': 'elif',
    'ForPrey': 'for',
    'WhileChasing': 'while',
    'Defur': 'def',
    'Fetch': 'return',
    'CatClass': 'class',
    'Paws': 'pass',
    'Scratch': 'break',
    'KeepGoing': 'continue',
    'WithWhiskers': 'with',
    'TryToCatch': 'try',
    'ExceptCat': 'except',
    'FinallyNap': 'finally',
    'CatCall': 'raise',
    'AssertCat': 'assert',
    'ImportCatnip': 'import',
    'FromCatTree': 'from',
    'Unleash': 'global',
    'Purrivate': 'nonlocal',
    'DeleteMouse': 'del',
    'Yowl': 'yield',
    'LambdaCat': 'lambda',
    'AwaitTreat': 'await',
    'AsyncPounce': 'async',
    
    # === LOGIC ===
    'AndCat': 'and',
    'OrCat': 'or', 
    'NotCat': 'not',
    'IsCat': 'is',
    'IsNotCat': 'is not',
    'InLitterbox': 'in',
    'NotInBox': 'not in',
    
    # === ASSIGNMENT OPERATORS ===
    'CatGets': '=',
    'PlusGets': '+=',
    'MinusGets': '-=',
    'TimesGets': '*=',
    'DivideGets': '/=',
    'FloorGets': '//=',
    'ModGets': '%=',
    'PowerGets': '**=',
    'WalrusCat': ':=',
    
    # === COMPARISON OPERATORS ===
    'SameAs': '==',
    'NotSame': '!=',
    'BiggerCat': '>',
    'SmallerCat': '<',
    'BiggerOrEqual': '>=',
    'SmallerOrEqual': '<=',
    
    # === ARITHMETIC OPERATORS ===
    'PlusCat': '+',
    'MinusCat': '-',
    'TimesCat': '*',
    'DivideCat': '/',
    'FloorCat': '//',
    'ModCat': '%',
    'PowerCat': '**',
    
    # === BUILT-IN FUNCTIONS ===
    'Meow': 'print',
    'Beg': 'input',
    'CountWhiskers': 'len',
    'CatType': 'type',
    'CatID': 'id',
    'HelpCat': 'help',
    'ListToys': 'dir',
    'ToCatYears': 'int',
    'ToFloatCat': 'float',
    'CatSpeak': 'str',
    'IsAwake': 'bool',
    'CatList': 'list',
    'CatTangle': 'tuple',
    'CatDiary': 'dict',
    'CatCollection': 'set',
    'CatBytes': 'bytes',
    'CatterArray': 'bytearray',
    'ComplexCat': 'complex',
    'CatAbs': 'abs',
    'CatSum': 'sum',
    'SmallestCat': 'min',
    'BiggestCat': 'max',
    'CatPower': 'pow',
    'RoundCat': 'round',
    'ShareTreats': 'divmod',
    'BinCat': 'bin',
    'OctoCat': 'oct',
    'HexCat': 'hex',
    'CatChar': 'chr',
    'CatOrder': 'ord',
    'CatHash': 'hash',
    'EnumerateMice': 'enumerate',
    'CatRange': 'range',
    'ZipCats': 'zip',
    'MapCat': 'map',
    'FilterCat': 'filter',
    'SortedCats': 'sorted',
    'ReverseCat': 'reversed',
    'CatIterator': 'iter',
    'NextToy': 'next',
    'CatSlice': 'slice',
    'AnyCat': 'any',
    'AllCats': 'all',
    'IsCatInstance': 'isinstance',
    'GetCatTrait': 'getattr',
    'SetCatTrait': 'setattr',
    'HasCatTrait': 'hasattr',
    'RemoveTrait': 'delattr',
    'CatProperty': 'property',
    'StaticCat': 'staticmethod',
    'ClassyCat': 'classmethod',
    'SuperCat': 'super',
    'CatEval': 'eval',
    'CatExec': 'exec',
    'CompileCat': 'compile',
    'OpenCatDoor': 'open',
    'CatMemory': 'memoryview',
    'LocalCats': 'locals',
    'GlobalCats': 'globals',
    'CatVars': 'vars',
    'CallableCat': 'callable',
    'CatRepr': 'repr',
    'CatFormat': 'format',
    'BreakTime': 'breakpoint',
    'FetchCatnip': '__import__',
    
    # === SPECIAL FUNCTIONS ===
    'Purr': '_cat_happy_print',
    'Hiss': '_cat_angry_print',
    'CatNap': '_cat_sleep',
    'Pounce': 'print',
    'ChaseMouse': '_chase_mouse',
    'RandomCat': '_random_cat',
    'CatNow': '_cat_now',
    
    # === CONSTANTS ===
    'Mew': 'False',
    'Catnap': 'None',
    'Pawsitive': 'True',
    'NineLives': '9',
    'CatPi': '3.14159',
    'EmptyFoodBowl': "''",
    'NoMice': '[]',
    'NoCatnip': '{}',
}

# Special handlers for functions that need extra processing
SPECIAL_HANDLERS = ['Purr', 'Hiss', 'CatNap', 'ChaseMouse', 'RandomCat', 'CatNow']

def translate(code: str) -> str:
    """Convert PyCat to Python with special handling"""
    # First pass: replace all regular keywords
    for cat_word, python_word in CAT_TO_PYTHON.items():
        if cat_word not in SPECIAL_HANDLERS:
            # Replace whole words only (using word boundaries)
            import re
            pattern = r'\b' + re.escape(cat_word) + r'\b'
            code = re.sub(pattern, python_word, code)
    
    # Second pass: handle special functions
    code = code.replace('Purr(', 'print(":3 " + str(')
    code = code.replace('Hiss(', 'print(":( " + str(')
    code = code.replace('CatNap(', 'time.sleep(')
    code = code.replace("ChaseMouse()", "'bonuscats'")
    code = code.replace("RandomCat()", "'cat'")
    code = code.replace('CatNow()', 'datetime.datetime.now()')
    
    # Add imports if needed
    if 'time.sleep' in code:
        code = 'import time\n' + code
    if 'random.choice' in code:
        code = 'import random\n' + code
    if 'datetime.datetime.now' in code:
        code = 'import datetime\n' + code
    
    return code
