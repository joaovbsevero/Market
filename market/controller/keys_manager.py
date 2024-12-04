from ..model.database_keys import DatabaseKeys


class KeysManager:
    def __init__(self):
        self.database_keys = DatabaseKeys()
        self.last_key = None

    def get_username_password(self, enterprise):
        return self.database_keys.get_username_password(enterprise)