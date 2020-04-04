import pytest

from .. import deserialize, InvalidJsonException
import json as sample_json


@pytest.mark.parametrize("test_input", [
    '"asd"',
    '123',
    '123.123123123',
    'true',
    '{"a":"b"}',
    '[1,2,"3",4,null,true]',
    '["a","b",2.34,{"a":2,"b":5},{"a":123},{"a":[1,2,3,{"a":{"asd":"hello"}}]}]',
])
def test_deserialize(test_input):
    assert deserialize(test_input) == sample_json.loads(test_input)


@pytest.mark.parametrize("test_input", [
    '[123,"asd"',
    '123,"asd"]',
    '[,123]',
    '{"123":,"asd":123}',
    '{"a":"asd":123',
    '{"a":"b",}',
    '{"a:"b"}'
])
def test_invalid_deserialize(test_input):
    with pytest.raises(InvalidJsonException):
        deserialize(test_input)
