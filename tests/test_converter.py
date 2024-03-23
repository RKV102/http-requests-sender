from curl_converter.converter import convert
from tests import get_fixture_content


def test_convert():
    assert (convert([get_fixture_content('input.txt')])
            == get_fixture_content('output.txt').split('\n'))
