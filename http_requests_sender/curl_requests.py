from progress.counter import Counter
from time import sleep


def build_curl_requests(http_requests, first_request_num,
                        last_request_num, host):
    for num, http_request in enumerate(http_requests, start=1):
        if num < first_request_num:
            continue
        if num > last_request_num:
            break
        method = http_request.get_method()
        url = to_curl_url(http_request.get_url(), host)
        query = http_request.get_query()
        body = http_request.get_body()
        headers = to_curl_headers(http_request.get_headers(), host)
        data = to_curl_data(query, body)
        curl_request = ['curl', '-X', method, *data, *headers, url]
        yield curl_request


def to_curl_url(plain_url, host):
    if host is None:
        return plain_url
    return plain_url.replace('localhost', host, 1)


def to_curl_data(query, body):
    if body:
        return '-d', body
    return '-G', '-d', query


def to_curl_headers(plain_headers, host):
    return (elem for list_ in (to_curl_header(plain_header, host)
            for plain_header in plain_headers) for elem in list_)


def to_curl_header(plain_header, host):
    if host is None or 'localhost' not in plain_header:
        return '-H', plain_header
    return '-H', plain_header.replace('localhost', host, 1)


def send_curl_requests(curl_requests, sender, stdout, stderr):
    sent_requests_counter = Counter('Sent requests: ')
    unsent_requests_count = 0
    for curl_request in curl_requests:
        status_code = sender(
            args=curl_request, stdout=stdout, stderr=stderr
        ).returncode
        if status_code in (0, 23):
            sent_requests_counter.next()
            sleep(1.0)
        else:
            unsent_requests_count += 1
    sent_requests_counter.finish()
    if unsent_requests_count:
        print(f'Unsent requests: {unsent_requests_count}')
