registry = {}

def register(cls):
    registry[cls.__name__] = cls.pattern

class Pattern(type):
    def __new__(cls, clsname, bases, attrs):
        newclass = super(Pattern, cls).__new__(cls, clsname, bases, attrs)
        register(newclass)
        return newclass
