import person
import os


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


class Display:
    contact_list = []
    command: str = ""
    messages = dict(empty="""
            ---------------------------
            🗑__Contact List is Empty__🗑
            ---------------------------
            """, invalid_command="""
            -------------------------
            ❌__Command not Valid__❌
            -------------------------
            """, invalid_id="""
            ------------------
            ❌__Invalid id__❌
            ------------------
            """, contact_saved="""
            --------------------
            Contact has saved ✅
            --------------------
            """, contact_clear="""
            ---------------------------
            Contact List has Cleared ✅
            ---------------------------
        """, remove= """
            ---------------------
            Contact has removed ✅
            ---------------------
        """, help="""
            =========================================
            Commands -
            * Type "show" for show all list
            * Type "add" for add a contact
            * Type "remove" <id> for remove a contact
            * Type "edit" <id> for edit a contact
            * Type "clear" for clear all contacts
            * Type "exit" for exit the program
            =========================================
        """)

    @staticmethod
    def contact_display(contact: object) -> str:
        socials = ""

        for social in contact.get_socials():
            socials += f"""
            ==========================
            name: {social.get_name()}
            url: {social.get_url()}
            ==========================
            """

        return f"""
        ------------------------------
        name: {contact.get_name()}
        email: {contact.get_email()}
        phone: {contact.get_phone()}
        location: {contact.get_location()}
        id: {contact.get_id()}
        socials ->
        {socials}
        ------------------------------
        """

    @staticmethod
    def set_social(contact: object) -> None:
        number_of_social: int = int(input("Enter the number of social link: "))

        for i in range(number_of_social):
            social_name: str = input(f"Enter social name {i + len(contact.get_socials())}: ")
            username: str = f"https://www.{social_name.lower()}.com/{input(f'Enter the {social_name} username: ')}"

            contact.set_socials(social_name, username)

    @staticmethod
    def __print_property(prop_name: str, properties: list) -> int:
        # print properties
        for prop in properties:
            print(f"{properties.index(prop)}. {prop}")

        return int(input(f"Select the {prop_name} that you would like to edit: "))

    @staticmethod
    def find_index(items: list, func) -> int:
        for item in items:
            if func(item):
                return items.index(item)
        return -1


    def start(self) -> None:
        clear()
        while self.command != "exit .":
            print("__Type help for show the valid commands__")
            self.command = input("Enter your command: ") + " .".lower()

            split_command = self.command.split(" ")
            clear()

            if split_command[0] == "add":
                self.__add()
            elif split_command[0] == "remove":
                self.__remove(split_command[1])
            # elif split_command[0] == "edit":
            #     self.__edit(split_command[1])
            elif split_command[0] == "clear":
                self.__clear()
            elif split_command[0] == "show":
                self.__show_list()
            elif split_command[0] == "help":
                self.__help()
            elif split_command[0] == "exit":
                print("Closing...")
            else:
                print(self.messages.get("invalid_command"))

    def __show_list(self) -> None:
        if len(self.contact_list) == 0:
            print(self.messages.get("empty"))
            return

        print("=========== Contact List ===========")
        for contact in self.contact_list:
            print(self.contact_display(contact))
        print("====================================")

    def __add(self) -> None:
        print("""
        ___Add Contact___
        """)
        name: str = input("Enter name: ")
        email: str = input("Enter email: ")
        phone: str = input("Enter phone: ")
        location: str = input("Enter location: ")
        contact: object = person.Person(name, email, phone, location)

        # add social link to contact
        self.set_social(contact)

        # add contact to contact list
        self.contact_list.append(contact)
        clear()
        print(self.messages.get("contact_saved"))

    def __remove(self, uuid: str):
        contact_index: int = self.find_index(
            self.contact_list,
            lambda obj: str(obj.get_id()) == uuid
        )

        if contact_index != -1:
            self.contact_list.remove(self.contact_list[contact_index])
            print(self.messages.get("remove"))
        else:
            print(self.messages.get("invalid_id"))

    # def __edit(self, uuid: str) -> None:

    def __help(self) -> None:
        print(self.messages.get("help"))

    def __clear(self) -> None:
        self.contact_list.clear()
        print(self.messages.get("contact_clear"))
