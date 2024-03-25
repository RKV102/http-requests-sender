from http_requests_sender import get_files_contents
from http_requests_sender.http_requests import get_http_requests
from http_requests_sender.curl_requests import (build_curl_requests,
                                                send_curl_requests)
import subprocess


def send_http_requests(files,
                       destination_ip,
                       request_sender=subprocess.run,
                       request_sender_stdout=subprocess.DEVNULL):
    contents = get_files_contents(files)
    http_requests = get_http_requests(contents)
    curl_requests = build_curl_requests(http_requests, destination_ip)
    send_curl_requests(curl_requests, request_sender, request_sender_stdout)
