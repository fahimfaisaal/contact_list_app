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

    def set_url(self, social_name: str, username: str = None):
        username = username or self.url.split("/")[-1]

        url = f"https://www.{social_name.lower()}.com/{username}"
        self.url = url
