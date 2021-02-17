import requests
import json


def display_main_menu():
    print("--- Main Menu ---")
    print("1) Prefix Calculator")
    print("2) Infix Calculator")


def prefix(cmd):
    data = json.dumps({"cmd": cmd})
    response = requests.post(
        "http://localhost:5000/prefix",
        json=data
    ).json()
    return response


def prefix_user():
    while True:
        cmd = input("Enter your prefix operation (or enter 'b' to go back)\n")
        if cmd == 'b':
            break
        print("The answer is: {}".format(prefix(cmd)))


def infix(cmd):
    data = json.dumps({"cmd": cmd})
    response = requests.post(
        "http://localhost:5000/infix",
        json=data
    ).json()
    return response


def infix_user():
    while True:
        cmd = input("Enter your infix operation (or enter 'b' to go back)\n")
        if cmd == 'b':
            break
        print("The answer is: {}".format(infix(cmd)))


def main():
    while True:
        display_main_menu()
        choice = input("Enter selection: ")
        if choice == "1":
            prefix()
        elif choice == "2":
            infix()
        else:
            print("Invalid selection")


if __name__ == "__main__":
    main()
