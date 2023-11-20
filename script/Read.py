##this file reads select lines from a credential file but is nto secure yet.

class Read:
    def __init__(self, filename):
        self.filename = filename
        self.__lines__ = []
        self.read()

    def read(self):
        with open(self.filename) as file:
            self.__lines__ = [line.strip() for line in file.readlines()]

    def cons_API_Key(self):
        return self.__lines__[0]

    def cons_API_secret(self):
        return self.__lines__[1]

    def access_token(self):
        return self.__lines__[2]

    def access_token_secret(self):
        return self.__lines__[3]

    def bearer_token(self):
        return self.__lines__[5]

    def Oauth_token(self):
        return self.__lines__[8]

    def Oauth_token_secret(self):
        return self.__lines__[9]

