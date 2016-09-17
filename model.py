# -*- coding: utf8 -*-


class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        if name == Model.__class__.__name__:
            return type.__new__(cls, name, bases, attrs)
        # check
        if 'table' not in attrs:
            attrs['table'] = name
        columns = []
        columns.extend(list(attrs.get('pk')))
        columns.extend(list(attrs.get('columns')))
        attrs['all_columns'] = set(columns)
        if len(attrs['all_columns']) == 0:
            raise RuntimeError(u'Columns should defined in class:{0}'.format(name))
        return type.__new__(cls, name, bases, attrs)


class Model(object):
    def __new__(cls, attrs, *args, **kwds):
        obj = super(Model, cls).__new__(cls, *args, **kwds)
        obj._attrs = attrs
        for k, v in obj.attrs:
            setattr(obj, k, v)
        return obj

    def __init__(self, *args, **kwds):
        raise RuntimeError('Can not be instantiated directly')

    def attrs(self):
        return self._attrs

    @classmethod
    def new(cls, attrs=None):
        attrs = {} if attrs is None else attrs
        if not isinstance(attrs, dict):
            raise RuntimeError('attrs should be a dict')
        for k, v in attrs:
            if k not in cls.all_columns:
                raise RuntimeError('{k} no in columns'.format(k=k))
        return cls.__new__(cls, attrs)

    @classmethod
    def select(cls, columns, **kwds):
        """get a row with query conditions
        """
        if not kwds or len(kwds) == 0:
            return None
        if not columns or len(columns) == 0:
            columns = cls.all_columns

        for col in columns:
            if col not in cls.all_columns:
                raise RuntimeError(u'column: {0} not defined in Model: {1}'.format(col,
                    cls.__name__))

        cond = []
        for k in kwds.keys():
            if k not in cls.all_columns:
                return None
            cond.append('{0}=%({0})s'.format(k))
        cols = ','.join(columns)
        condition = ' AND '.join(cond)
        sql = """SELECT {0} FROM {1}
                 WHERE {2}
                 """.format(cols, cls.table, condition)
        pass

   @classmethod
   def select_list(cls, columns, **kwnds):
       """get many rows with query conditions
       """
       pass

   def insert(self):
       """
       """
       pass

   @classmethod
   def insert_list(cls, rows):
       """
       """
       pass

   def update(self, **kwds):
       """
       """
       pass

   @classmethod
   def update_list(cls, rows):
       """
       """
       pass

   def delete(self):
       """
       """
       pass

   @classmethod
   def delete_list(cls, **kwds):
       """
       """
       pass

   @classmethod
   def paginate(cls, curpage=-1, pagesize=10,
                condition=None, orderby=None):
       """return results by pagination;

       Params:
           curpage -- current page
           pagesize -- items size
           condition -- query condition, should be dict
           orderby -- ORDER BY

       Return:
           a dict -- data sample,
                {
                    'curpage': 10,
                    'pagesize': 10,
                    'count': 100
                    'rows': [{
                         'col1': 'xxxx',
                         ...
                         },
                         ...
                    ]
                }
       """
       pass
