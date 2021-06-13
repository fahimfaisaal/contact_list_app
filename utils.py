import os
import json
from typing import Union
from Classes import person


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


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
        -------------------------------------
        name: {contact.get_name()}
        email: {contact.get_email()}
        phone: {contact.get_phone()}
        location: {contact.get_location()}
        id: {contact.get_id()}
        socials ->
        number of socials -> {str(len(contact.get_socials()))}
        {socials}
        -------------------------------------
        """


def set_social_by_user(contact: object) -> None:
    number_of_social: int = int(input("Enter the number of social link: "))

    for i in range(number_of_social):
        social_name: str = input(f"Enter social name {len(contact.get_socials()) + 1}: ")
        username: str = f"https://www.{social_name.lower()}.com/{input(f'Enter the {social_name.lower()} username: ')}"

        contact.set_socials(social_name, username)


def print_property(prop_name: str, properties: Union[list, tuple]) -> int:
    # print properties
    for prop in properties:
        print(f"{properties.index(prop) + 1}.{prop}")

    option: int = int(input(f"Select the {prop_name} that you would like to edit: "))

    if option < 1 or option > len(properties):
        print("execute")
        return -1

    return option


def find_index(items: list, func) -> int:
    for item in items:
        if func(item):
            return items.index(item)
    return -1


def generate_message(message: str):
    return f"""
    -----------------------------
    {message}
    -----------------------------
    """


# storage controller
def read_contacts(contact_list: list) -> None:
    try:
        json_object = open("./contacts/data.json", "r")
        contacts = json.loads(json_object.read())

        for contact in contacts:
            person_obj_from_dic: object = person.Person(
                contact.get("name"),
                contact.get("email"),
                contact.get("phone"),
                contact.get("location")
            )

            person_obj_from_dic.set_id(contact.get("id"))
            socials: list = contact.get("socials")

            if len(socials):
                for social_dic in socials:
                    person_obj_from_dic.set_socials(
                        social_dic.get("name"),
                        social_dic.get("url")
                    )

            contact_list.append(person_obj_from_dic)
    except:
        pass


def write_contacts(contact_list: list) -> None:
    parse_dict_contacts: list = []

    # object to dictionary
    for contact in contact_list:
        parse_dict_contacts.append(contact.to_dictionary())

    # parse dictionary to json
    contacts_json = json.dumps(parse_dict_contacts, indent=3)
    # open file in contacts
    json_file = open("./contacts/data.json", "w")
    # save it to the current path
    json_file.write(contacts_json)
    json_file.close()
