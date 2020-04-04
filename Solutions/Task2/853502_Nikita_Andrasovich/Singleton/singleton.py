# Implement Singleton pattern
class SingletonTemplate(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                SingletonTemplate, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
