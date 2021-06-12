import uuid


class Person:
    name = ""
    email = ""
    phone = ""
    location = ""

    def __init__(self, *details):
        self.name = details[0]
        self.email = details[1]
        self.phone = details[2]
        self.location = details[3]
        # Auto construct
        self.id = uuid.uuid1()
        self.socials = []

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email: str):
        self.email = email

    def get_phone(self):
        return self.phone

    def set_phone(self, phone: str):
        self.phone = phone

    def get_location(self):
        return self.location

    def set_location(self, location: str):
        self.location = location

    def get_socials(self):
        return self.socials

    def set_socials(self, social_name: str, url: str):
        self.socials.append(Social(social_name, url))

    def get_id(self):
        return self.id


class Social:
    name = ""
    url = ""

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def get_name(self):
        return self.name

    def set_name(self, social_name: str):
        self.name = social_name

    def get_url(self):
        return self.url

    def set_url(self, social_name: str, username: str):
        url = f"https://www.{social_name}.com/{username}"
        self.url = url
