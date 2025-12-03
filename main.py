from adress_book import (
    AddressBook,
    parse_input,
    COMMANDS
    )


def main():
    try:
        book = AddressBook()
        print("Welcome to the assistant bot!")
        while True:
            user_input = input("Enter a command: ").strip()
            if not user_input:
                print("Enter a command please.")
                continue

            command, args = parse_input(user_input)
            if command in COMMANDS:
                result = COMMANDS[command](args, book)
                print(result)
                if command in ["close", "exit"]:
                    print("Good bye!")
                    break
            else:
                print("Invalid command.")
    except Exception as err:
        print(f"Error: {err}")

if __name__ == '__main__':
    main()