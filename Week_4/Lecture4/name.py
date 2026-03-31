import sys

# sys.argv

# in the sys module, theres a pre built variable
# called argv = argument vector.
#
# It means the list of all the words user typed before
# they hit ENTER.

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
    # sys.exit exits program here itself

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

# remember, argv is a list

# the actual first thing in the .argv variable is the file name we enter

# now user can just enter a value beside the name.py command

# the program can crash if the usre doesnt enter anythign
# because of index error