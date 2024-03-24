from http_requests_sender.http import get_http_requests
from http_requests_sender.curl import build_curl_requests, send_curl_requests


def send_http_requests(files):
    contents = get_file_contents(files)
    http_requests = get_http_requests(contents)
    curl_requests = build_curl_requests(http_requests)
    send_curl_requests(curl_requests)


def get_file_contents(file_paths):
    contents = []
    for file_path in file_paths:
        with open(file_path) as file:
            contents.append(file.read())
    return contents
