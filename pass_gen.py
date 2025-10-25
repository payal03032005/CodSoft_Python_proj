import random
import string

print("\n\t***PASSWORD GENERATOR APP***")
print("\tby @PAYAL RAMDAS SUNE\n")


def gen_password(length):
    characters = (
        string.digits + string.punctuation + string.hexdigits + string.ascii_letters
    )
    password = "".join(random.choice(characters) for _ in range(length))
    return password


num_suffix = (
    lambda n: "th"
    if 10 <= n % 100 <= 20
    else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
)


def main():
    try:
        password_length = int(input("Enter the desired length of the password: "))

        if password_length <= 0:
            print("Please enter a valid password length.")
            return

        for _ in range(1):
            password = gen_password(password_length)
            print("Password: ", password)

    except ValueError:
        print("Please enter a valid integer for the password length.")


if __name__ == "__main__":
    main()