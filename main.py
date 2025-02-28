def get_pin():
    while True:
        pin = input("Please enter a 4-digit PIN: ")
        if len(pin) == 4 and pin.isdigit():
            return pin
        else:
            print("Invalid PIN. Please ensure it is exactly 4 digits long and contains only numbers.")

def save_pin(pin):
    with open("pin_file.txt", "w") as file:
        file.write(pin)
    print("PIN saved successfully.")

def verify_pin(stored_pin):
    input_pin = get_pin()
    if input_pin == stored_pin:
        print("Access granted. You can now view the file content.")
        return True
    else:
        print("Access denied. Incorrect PIN.")
        return False

def open_file():
    try:
        with open("file_3.txt", "r") as file:
            content = file.read()
        print("File content:\n", content)
    except FileNotFoundError:
        print("File not found. Please ensure 'file_3.txt' exists.")

def main():
    # Get and save the PIN
    pin = get_pin()
    save_pin(pin)

    # Prompt user to access the protected file
    print("\nNow, to access 'file_3.txt', please enter the PIN.")
    stored_pin = pin  # Store the pin to verify later

    if verify_pin(stored_pin):
        open_file()

if __name__ == "__main__":
    main()

