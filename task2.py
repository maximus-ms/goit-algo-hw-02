from collections import deque


def is_palindrome(data):
    d = deque(data.replace(" ", "").lower())
    if len(d) == 0:
        raise Exception("No data")
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True


def main():
    while True:
        data = input("Please enter your phrase: ")
        try:
            print(f"is palindrome: {is_palindrome(data)}")
        except Exception as err:
            print(err)


if __name__ == "__main__":
    main()
