class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls.instance