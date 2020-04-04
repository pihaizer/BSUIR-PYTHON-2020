import pytest

from .. import serialize, serialize_pretty
import json as sample_json


class SomeClass:
    def __init__(self, a):
        self.a = a


class SomeClassEncoder(sample_json.JSONEncoder):
    def default(self, o):
        if isinstance(o, SomeClass):
            return o.__dict__
        return sample_json.JSONEncoder.default(self, o)


@pytest.mark.parametrize("test_input", [
    "123asd",
    123,
    True,
    [1, 2, [3, 4, 'asd', True], None, 3.45],
    {1: "asd", 2: "zxc"},
    ["a", "b", 2.34, {"a": 2, "b": 5}, SomeClass(123), SomeClass([1, 2, 3, SomeClass({"asd": "hello"})])]
])
def test_serialize(test_input):
    assert serialize(test_input) == sample_json.dumps(test_input, separators=(',', ':'), cls=SomeClassEncoder)


def test_serialize_pretty():
    serialized = serialize_pretty([1, 2, "123", [4, {"a": 5}]])
    assert serialized == """\
[
    1,
    2,
    "123",
    [
        4,
        {
            "a": 5
        }
    ]
]"""
