while True:
    try:
        num = int(input("Enter a number: "))
        print(f"You entered: {num}")
        break
    except ValueError:
        print("Not a number, try again")
    except EOFError:
        print("No input given, try again")
        break