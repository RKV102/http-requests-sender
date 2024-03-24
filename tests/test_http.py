from tests import get_fixture_content
from curl_converter.http import get_http_requests
from tests.fixtures.http_requests import http_requests as output_http_requests


def test_get_http_requests():
    input_http_requests = get_http_requests([get_fixture_content('input.txt')])
    for num, input_http_request in enumerate(input_http_requests):
        assert input_http_request.method == output_http_requests[num]['method']
        assert input_http_request.url == output_http_requests[num]['url']
        assert input_http_request.query == output_http_requests[num]['query']
        assert (input_http_request.headers
                == output_http_requests[num]['headers'])
        assert input_http_request.body == output_http_requests[num]['body']
