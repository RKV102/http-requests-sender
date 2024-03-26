from http_requests_sender.http_requests import get_http_requests
from http_requests_sender.curl_requests import (build_curl_requests,
                                                send_curl_requests)
import subprocess


def send_http_requests(contents,
                       destination_ip,
                       first_request,
                       last_request,
                       request_sender=subprocess.run,
                       request_sender_stdout=subprocess.DEVNULL,
                       request_sender_stderr=subprocess.DEVNULL):
    http_requests = get_http_requests(contents)
    curl_requests = build_curl_requests(http_requests, first_request,
                                        last_request, destination_ip)
    send_curl_requests(curl_requests, request_sender,
                       request_sender_stdout, request_sender_stderr)
