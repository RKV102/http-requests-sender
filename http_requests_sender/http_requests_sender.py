from http_requests_sender.http_requests import get_http_requests
from http_requests_sender.curl_requests import (to_curl_requests,
                                                send_curl_requests)
import subprocess


def send_http_requests(request_sender=subprocess.run,
                       request_sender_stdout=subprocess.DEVNULL,
                       request_sender_stderr=subprocess.DEVNULL,
                       **kwargs):
    contents, first_request_num, last_request_num, host = unpack_kwargs(kwargs)
    http_requests = get_http_requests(contents)
    curl_requests = to_curl_requests(http_requests,
                                     first_request_num,
                                     last_request_num,
                                     host)
    send_curl_requests(curl_requests, request_sender,
                       request_sender_stdout, request_sender_stderr)


def unpack_kwargs(kwargs):
    try:
        contents = kwargs['contents']
        first_request_num = kwargs['first_request_num']
        last_request_num = kwargs['last_request_num']
        host = kwargs['host']
    except KeyError:
        raise TypeError('send_http_requests() missing one of the following '
                        'required arguments: contents, first_request_num, '
                        'last_request_num, host')
    return contents, first_request_num, last_request_num, host
