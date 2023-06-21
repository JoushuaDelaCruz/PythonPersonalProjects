import random
import string


class PasswordGenerator:
    """
    PasswordGenerator is a class that generates a random password using
    the string module and random module.

    Attributes:
        __characters (str): A string containing all the characters that can be used to generate a password from the string module. 
    """
    __characters = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self, length: int, total_passwords: int) -> list:
        """
        A function that generates a random password using the string module and random module.
        Random module is used to choose random characters from the string module.

        :param length: the length of each password to be generated
        :param total_passwords: the total number of passwords to be generated
        :return: a list of randomly generated passwords
        """
        passwords = []
        for _ in range(total_passwords):
            password = ''
            for _ in range(length):
                password += random.choice(self.__characters)
            passwords.append(password)
        return passwords
