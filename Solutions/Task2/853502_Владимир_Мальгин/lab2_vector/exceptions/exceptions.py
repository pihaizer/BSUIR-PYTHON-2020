class VectorException(Exception):
    def __init__(self, message='Invalid lab2_vector'):
        self.message = message

    def __repr__(self):
        return self.message


class VectorSumException(VectorException):
    def __init__(self, message="Can't sum there vectors"):
        super(VectorSumException, self).__init__(message)


class VectorMulException(VectorException):
    def __init__(self, message="Can't multiply this lab2_vector", vector=None, multiplier=None):
        super(VectorMulException, self).__init__(message)
        if vector is not None and multiplier is not None:
            self.message += ": {0}, {1}".format(vector, multiplier)


class VectorScalarException(VectorException):
    def __init__(self, v1=None, v2=None):
        self.message = "Can't scalar multiply these vectors"
        if v1 is not None and v2 is not None:
            self.message += ": {0}, {1}".format(v1, v2)
