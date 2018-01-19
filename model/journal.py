from model import Model


class Journal(Model):

    @classmethod
    def valid_names(cls):
        names = super().valid_names()
        names = names + [
            ('title', str, ''),
            ('content', str, ''),
        ]
        return names

    @classmethod
    def from_file(cls, content):
        pass
