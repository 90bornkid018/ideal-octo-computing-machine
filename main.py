def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to the program."

def main():
    user_name = input("Enter your name: ")
    print(greet(user_name))

if __name__ == "__main__":
    main()
