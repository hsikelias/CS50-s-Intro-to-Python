import sys
import pyfiglet

# expects 0 or two command line arguments, 0  arguments gives random font.
# if arguments given then arg[1] is -f or --font, next argument is the name of the font
allowed_fonts = pyfiglet.FigletFont.getFonts()

if len(sys.argv) == 1 or len(sys.argv) == 3:
    if len(sys.argv) == 1:  # user enters nothing
        word = input("Input: ")
        print(f"Output: \n{pyfiglet.figlet_format(word)}")

    elif len(sys.argv) == 3:  # user enters -f or --font and font name
        if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in allowed_fonts:
            word = input("Input: ")
            print(f"Output: \n{pyfiglet.figlet_format(word, sys.argv[2])}")
            sys.exit()
        else:
            sys.exit("Can only use '-f' or '--font'")
else:
    sys.exit("Follow the format!")