from Classes import person
import utils


class Display:
    contact_list: list = []
    command: str = ""

    def start(self) -> None:
        utils.clear()

        utils.read_contacts(self.contact_list)

        while self.command != "exit .":
            print("__Type help for show the valid commands__")
            self.command = input("Enter your command: ") + " .".lower()

            split_command: list = self.command.split(" ")
            utils.clear()

            if split_command[0] == "add":
                self.__add()
            elif split_command[0] == "remove":
                self.__remove(split_command[1])
            elif split_command[0] == "edit":
                self.__edit(split_command[1])
            elif split_command[0] == "clear":
                self.__clear()
            elif split_command[0] == "show":
                self.__show_list()
            elif split_command[0] == "help":
                self.__help()
            elif split_command[0] == "exit":
                print("Closing...")
                utils.write_contacts(self.contact_list)
            else:
                print(utils.generate_message("❌__Invalid user command__❌"))

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
        utils.set_social_by_user(contact)

        # add contact to contact list
        self.contact_list.append(contact)
        print(utils.generate_message("✅__Contact has saved__✅"))

    def __show_list(self) -> None:
        # if contact list len is zero
        if len(self.contact_list) == 0:
            print(utils.generate_message("🗑__Contact List is Empty__🗑"))
            return

        # print contact list
        print("=========== Contact List ===========")
        for contact in self.contact_list:
            print(utils.contact_display(contact))
        print("====================================")

    def __edit(self, uuid: str) -> None:
        # find contact index via uuid
        find_index_via_uuid: int = utils.find_index(
            self.contact_list,
            lambda obj: obj.get_id() == uuid
        )

        # if object not found
        if find_index_via_uuid == -1:
            return print(utils.generate_message("❌_Invalid contact id_❌"))

        # object have to edit
        contact: object = self.contact_list[find_index_via_uuid]

        # options
        edit_options: tuple = ("name", "email", "phone", "location", "socials")

        get_edit_option: int = utils.print_property("property name", edit_options)

        # if option not found
        if get_edit_option == -1:
            utils.clear()
            print(utils.generate_message("❌___Invalid selection___❌"))

            return self.__edit(uuid)

        # if user selected 5, mean social
        if get_edit_option == 5:
            return self.__manage_social(contact.get_socials(), contact)



    def __manage_social(self, socials: list, contact: object) -> None:
        # if socials is empty
        if not len(socials):
            print(utils.generate_message("🗑____Empty social____🗑"))
            return

        # social edit options
        edit_options: tuple = ("add", "remove", "edit name", "edit username")
        utils.clear()
        get_edit_option = utils.print_property("option", edit_options)

        if get_edit_option == -1:
            utils.clear()
            print(utils.generate_message("❌___Invalid selection___❌"))

            return self.__manage_social(socials, contact)

        if get_edit_option == 1:
            return utils.set_social_by_user(contact)

        # social name that would like to edit
        social_name: str = input("Enter current social name: ")

        # fint the social object index by name
        edit_social_index: int = utils.find_index(
            socials,
            lambda obj: obj.get_name() == social_name
        )

        if edit_social_index == -1:
            utils.clear()
            print(utils.generate_message("❌_Invalid social name_❌"))

            return self.__manage_social(socials, contact)


        social: object = contact.get_socials()[edit_social_index]

        if get_edit_option == 2:
            contact.get_socials().remove(social)
        elif get_edit_option == 3:
            new_name = input("Enter new social name: ")

            social.set_name(new_name)
            social.set_url(social.get_name())
        else:
            social.set_url(social.get_name(), input("Enter new username: "))

        utils.clear()
        print(utils.generate_message("✅___Contact has updated___✅"))

    def __remove(self, uuid: str) -> None:
        # find contact index by uuid
        contact_index: int = utils.find_index(
            self.contact_list,
            lambda obj: str(obj.get_id()) == uuid
        )

       # if object found
        if contact_index != -1:
            self.contact_list.remove(self.contact_list[contact_index])
            print(utils.generate_message("✅__Contact has removed__✅"))
        else:
            # if object not found
            print(utils.generate_message("❌__Invalid contact id__❌"))

    def __help(self) -> None:
        print("""
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

    def __clear(self) -> None:
        self.contact_list.clear()
        print(utils.generate_message("✅__Contact has cleared__✅"))
