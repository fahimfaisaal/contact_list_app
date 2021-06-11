import uuid


class Person:
    name = ""
    email = ""
    phone = ""
    location = ""
    id = ""

    def __init__(self, *details):
        self.name = details[0]
        self.email = details[1]
        self.phone = details[2]
        self.location = details[3]
        self.id = uuid.uuid1()
        self.social = []

    def __get_name__(self):
        return self.name

    def __set_name__(self, name: str):
        self.name = name

    def __get_email__(self):
        return self.email

    def __set_email__(self, email: str):
        self.email = email

    def __get_phone__(self):
        return self.phone

    def __set_phone__(self, phone: str):
        self.phone = phone

    def __get_location__(self):
        return self.location

    def __set_location__(self, location: str):
        self.location = location

    def __get_social__(self):
        return self.social

    def __set_social__(self, social_name: str, url: str):
        self.social.append(Social(social_name, url))

    def __get_id__(self):
        return self.id


class Social:
    name = ""
    url = ""

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def __get_name__(self):
        return self.name

    def __set__social_name__(self, social_name: str):
        self.name = social_name

    def __get_url__(self):
        return self.url

    def __set__url__(self, url: str):
        self.url = url
