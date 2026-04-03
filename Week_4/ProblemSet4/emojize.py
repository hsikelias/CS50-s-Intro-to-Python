import emoji


def main():
    try:
        emojicode = input("Input: ")
        print(f"Output: {emoji.emojize(emojicode, language='alias')}")
    except:
        EOFError
        KeyboardInterrupt


main()
