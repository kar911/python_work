import sys
from getopt import getopt


def fun():
    """
dasdasdsad
    """
    sd = None
    ed = None
    argv = sys.argv[1:]
    d=["dev=", "def="]
    opts,remargs = getopt(argv, 'a:x:',d)  # long option must have " = " sign just to let it accept not supported in 3.8

    for opt, args in opts:
        if opt in ['--dev', '-a']:  # long option '--dev' followed with short '-a' just to specifie
            sd = args
        elif opt in ['--def', '-x']:
            ed = args
    print(f"start date {sd}")
    print(f"end date {ed}")


fun()