from password_generator import PasswordGenerator


class FrontEnd:
    def display(self):
        print("Welcome to Password Generator!")
        length = int(input("Enter the length of the password: "))
        total_passwords = int(
            input("Enter the total number of passwords to be generated: "))
        passwords = PasswordGenerator().generate_password(length, total_passwords)
        print("Here are your passwords: ")
        print(*passwords, sep='\n')


def main():
    FrontEnd().display()


if __name__ == '__main__':
    main()
