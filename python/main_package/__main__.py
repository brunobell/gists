"""
'__main__' is the name of the scope in which top-level code executes.
A module's __name__ is set equal to '__main__' when read from standard input,
a script, or from an interactive prompt.

For a package, the same effect can be achieved by including a __main__.py
module, the contents of which will be executed when the module is run with -m.
"""

print('this will always be printed')


if __name__ == '__main__':
    print('this script is running in the main scope')
