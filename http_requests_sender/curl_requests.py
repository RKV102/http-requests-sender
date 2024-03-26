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
        url = http_request.get_url() if host is None\
            else http_request.get_url().replace('localhost', host, 1)
        query = http_request.get_query()
        headers = (
            header if host is None
            else header.replace('localhost', host, 1)
            for header in http_request.get_headers()
        )
        body = http_request.get_body()
        curl_request = ['curl', '-X', method]
        if body:
            curl_request = [*curl_request, '-d', body]
        elif query:
            curl_request = [*curl_request, '-G', '-d', query]
        curl_request = [*curl_request, *(
            j for i in (('-H', header) for header in headers) for j in i
        ), url]
        yield curl_request


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
