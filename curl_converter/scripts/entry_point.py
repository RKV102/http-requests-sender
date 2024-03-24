from curl_converter import get_files, get_files_content
from curl_converter.http import get_http_requests
from curl_converter.curl import send_curl_requests, build_curl_requests


def main():
    files = get_files()
    contents = get_files_content(files)
    http_requests = get_http_requests(contents)
    curl_requests = build_curl_requests(http_requests)
    send_curl_requests(curl_requests)


if __name__ == '__main__':
    main()
