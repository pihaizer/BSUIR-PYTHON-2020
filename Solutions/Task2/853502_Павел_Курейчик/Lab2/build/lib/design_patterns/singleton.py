import threading


class SingletonMeta(type):
    __instance = None
    __mutex = threading.RLock()

    def __call__(cls, *args, **kwargs):
        with cls.__mutex:
            if not cls.__instance:
                cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance
