class InvalidJsonException(Exception):
    def __str__(self):
        return 'Invalid JSON string'
