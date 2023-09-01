class User:

    def __init__(self, tg_id: int, username: str, lang: str) -> None:
        self.id = tg_id
        self.username = username
        self.lang = lang
