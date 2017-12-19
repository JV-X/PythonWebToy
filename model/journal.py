class Journal(object):
    def __init__(self, date='',
                 display_date='', year='',
                 name='', display_name='', content=''):
        self.date = date
        self.display_date = display_date
        self.year = year
        self.name = name
        self.display_name = display_name
        self.content = content

    @staticmethod
    def all():
        js = (
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
        )
        return js