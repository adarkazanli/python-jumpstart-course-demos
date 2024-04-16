def print_header():
    print("--------------------------------")
    print("           HELLO APP")
    print("--------------------------------")
    print()


def print_footer(name: str):
    message = f"Have a nice day {name}!"
    print()
    print("-" * (len(message) + 12))
    print(" " * 6, message)
    print("-" * (len(message) + 12))


def main():
    print_header()
    ask_name = input("What is your name?  ")
    if len(ask_name) == 0:
        print("You didn't enter your name")
    print_footer(ask_name)


if __name__ == "__main__":
    main()
