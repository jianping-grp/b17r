def register(r_cls):
    print 'register'
    print r_cls.__name__
    def _wrapper(cls):
        print cls.__name__
        setattr(r_cls, 'test', len(cls.__name__))
        print dir(r_cls)
        return cls
    return _wrapper