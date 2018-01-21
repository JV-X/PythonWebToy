from model import Model, replace_new_line_character


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

    @classmethod
    def find_by_id(cls, id):
        id = int(id)
        j = Journal.find_by(id=id)[0]
        j.content = replace_new_line_character(j.content)
        return j