import cowsay
import sys


if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.orig_argv[1:])