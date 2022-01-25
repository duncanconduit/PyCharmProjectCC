
def value_error():
    while True:
        try:
            start = int(input(""))
            break

        except ValueError:
            print("Error: Not a Valid Answer  Try again...")
    return start



