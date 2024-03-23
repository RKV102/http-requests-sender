from curl_converter.http import get_http_requests, build_curl_requests


def convert(contents):
    http_requests = get_http_requests(contents)
    curl_requests = build_curl_requests(http_requests)
    return curl_requests
