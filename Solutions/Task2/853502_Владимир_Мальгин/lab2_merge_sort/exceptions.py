class MergeSortError(Exception):
    def __init__(self, message='Invalid lab2_vector'):
        self.message = message

    def __repr__(self):
        return self.message
