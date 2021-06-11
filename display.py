import person
import os


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


class Display:
    contact_list = []
    command: str = ""
    messages = {
        "empty": """
            ---------------------------
            🗑__Contact List is Empty__🗑
            ---------------------------
            """,
        "invalid_command": """
            -------------------------
            ❌__Command not Valid__❌
            -------------------------
            """,
        "contact_saved": """
            --------------------
            Contact has saved ✅
            --------------------
            """,
        "contact_clear": """
            ---------------------------
            Contact List has Cleared ✅
            ---------------------------
        """,
        "help": """
            ========================================
            Commands -
            * Type "show" for show all list
            * Type "add" for add a contact
            * Type "remove" <id> for remove a contact
            * Type "edit" <id> for edit a contact
            * Type "clear" for clear all contacts
            ========================================
        """
    }

    @staticmethod
    def contact_display(contact: object):
        socials = ""

        for social in contact.__get_social__():
            socials += f"""
            ====================
            name: {social.__get_name__()}
            url: {social.__get_url__()}
            ====================
            """

        return f"""
        ------------------------------
        name: {contact.__get_name__()}
        email: {contact.__get_email__()}
        phone: {contact.__get_phone__()}
        location: {contact.__get_location__()}
        id: {contact.__get_id__()}
        socials ->
        {socials}
        ------------------------------
        """

    def start(self):
        while self.command != "exit .":
            print("__Type help for show the valid commands__")
            self.command = input("Enter your command: ") + " .".lower()

            split_command = self.command.split(" ")
            clear()

            if split_command[0] == "add":
                self.__add__()
            # elif split_command[0] == "remove":
            #     self.__remove__(split_command[1])
            # elif split_command[0] == "edit":
            #     self.__remove__(split_command[1])
            elif split_command[0] == "clear":
                self.__clear__()
            elif split_command[0] == "show":
                self.__show_list__()
            elif split_command[0] == "help":
                self.__help__()
            elif split_command[0] == "exit":
                print("Closing...")
            else:
                print(self.messages.get("invalid_command"))

    def __show_list__(self):
        if len(self.contact_list) == 0:
            print(self.messages.get("empty"))
            return

        print("=========== Contact List ===========")
        for contact in self.contact_list:
            print(self.contact_display(contact))
        print("====================================")

    def __add__(self):
        print("""
        ___Add Contact___
        """)
        name = input("Enter name: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        location = input("Enter location: ")
        number_of_social = int(input("Enter the number of social link: "))

        contact = person.Person(name, email, phone, location)

        for i in range(number_of_social):
            social_name = input(f"Enter social name {i + 1}: ")
            url = input(f"Enter the url of your {social_name}: ")
            contact.__set_social__(social_name, url)

        self.contact_list.append(contact)
        clear()
        print(self.messages.get("contact_saved"))

    # def __remove__(self, id: str):
    #
    #
    # def __edit__(self, id: str):

    def __help__(self):
        print(self.messages.get("help"))

    def __clear__(self):
        self.contact_list.clear()
        print(self.messages.get("contact_clear"))
