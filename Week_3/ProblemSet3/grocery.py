item_list = []
used = []


def main():
    while True:
        try:
            item = input().upper()
            item_list.append(item)
        except:
            EOFError
            break

    for item in sorted(item_list):
        if item not in used:
            item_count = item_list.count(item)
            print(f"{item_count} {item}")
            used.append(item)

main()