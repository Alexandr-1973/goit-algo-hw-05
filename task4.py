def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            if func.__name__=="add_contact":
                return ("Enter the argument for the command\n"
                        "Correct format for input: 'add [name] [phone number]'")
            if func.__name__=="change_contact":
                return ("Enter the argument for the command\n"
                        "Correct format for input: 'change [name] [new phone number]'")
            if func.__name__=="show_phone":
                return ("Enter the argument for the command\n"
                        "Correct format for input: 'phone [name]'")
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error. Contact not found"

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{contacts[name]}"
    else:
        return "Error. Contact not found"

def show_all(contacts):
    contacts_pretty_string="\n All contacts:\n"
    for k,v in contacts.items():
        contacts_pretty_string+=f"{k} {v}\n"
    return contacts_pretty_string

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()