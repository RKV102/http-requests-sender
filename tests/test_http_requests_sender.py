from http_requests_sender.http_requests_sender import send_http_requests
from tests import get_fixture_content
from tests.fixtures.curl_requests import curl_requests
from unittest.mock import Mock


def test_send_http_requests():
    mock = Mock()
    send_http_requests(
        contents=[get_fixture_content('input.txt')],
        destination_ip='192.168.1.45',
        first_request_num=2,
        last_request_num=4,
        request_sender=mock,
        request_sender_stdout=None,
        request_sender_stderr=None
    )
    assert mock.call_args_list == [
        ({'args': curl_requests[0], 'stdout': None, 'stderr': None},),
        ({'args': curl_requests[1], 'stdout': None, 'stderr': None},),
        ({'args': curl_requests[2], 'stdout': None, 'stderr': None},)
    ]
