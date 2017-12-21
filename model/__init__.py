import time

from pymongo import MongoClient

from utils import log


def timestamp():
    return int(time.time())


db_client = MongoClient()


def next_id(name):
    query = {
        'name': name,
    }
    update = {
        '$inc': {
            'seq': 1
        }
    }
    kwargs = {
        'query': query,
        'update': update,
        'upsert': True,
        'new': True,
    }
    doc = db_client.db['data_id']

    new_id = doc.find_and_modify(**kwargs).get('seq')
    return new_id


class Model(object):
    @classmethod
    def valid_names(cls):
        names = [
            '_id',
            ('id', int, -1),
            ('deleted', bool, False),
            ('created_time', int, 0),
            ('updated_time', int, 0),
        ]
        return names

    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{0} = {1}'.format(k, v) for k, v in self.__dict__.items())
        return '<{0}: \n  {1}\n>'.format(class_name, '\n  '.join(properties))

    @classmethod
    def new(cls, form=None, **kwargs):
        name = cls.__name__
        m = cls()
        names = cls.valid_names().copy()
        names.remove('_id')
        if form is None:
            form = {}

        for f in names:
            k, t, v = f
            if k in form:
                setattr(m, k, t(form[k]))
            else:
                setattr(m, k, v)
        for k, v in kwargs.items():
            if hasattr(m, k):
                setattr(m, k, v)
            else:
                raise KeyError
        m.id = next_id(name)
        ts = timestamp()
        m.created_time = ts
        m.updated_time = ts
        m.save()
        return m

    @classmethod
    def __new_from_db(cls, bson):
        m = cls()
        names = cls.valid_names().copy()
        # 去掉 _id 这个特殊的字段
        names.remove('_id')
        for f in names:
            k, t, v = f
            if k in bson:
                setattr(m, k, bson[k])
            else:
                setattr(m, k, v)
        setattr(m, '_id', bson['_id'])
        return m

    @classmethod
    def all(cls, **kwargs):
        return cls._find(**kwargs)

    #  还应该有一个函数 find(name, **kwargs)
    @classmethod
    def _find(cls, **kwargs):
        name = cls.__name__
        kwargs['deleted'] = False
        ds = db_client.db[name].find(kwargs)
        l = [cls.__new_from_db(d) for d in ds]
        return l

    @classmethod
    def find_by(cls, **kwargs):
        kwargs['deleted'] = False
        l = cls._find(**kwargs)
        return l

    @classmethod
    def find(cls, id):
        return cls.find_one(id=id)

    @classmethod
    def find_one(cls, **kwargs):
        kwargs['deleted'] = False
        l = cls._find(**kwargs)
        if len(l) > 0:
            return l[0]
        else:
            return None

    def save(self):
        name = self.__class__.__name__
        log.i("on save {}".format(self.__dict__))
        db_client.db[name].save(self.__dict__)

    def delete(self):
        name = self.__class__.__name__
        query = {
            'id': self.id,
        }
        values = {
            'deleted': True
        }
        db_client.db[name].update_one(query, values)

    def blacklist(self):
        b = [
            '_id',
        ]
        return b

    def json(self):
        _dict = self.__dict__
        d = {k: v for k, v in _dict.items() if k not in self.blacklist()}
        return d
