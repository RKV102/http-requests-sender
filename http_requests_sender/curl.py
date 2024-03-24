from os import system


def build_curl_requests(http_requests):
    curl_requests = []
    for http_request in http_requests:
        method = http_request.get_method()
        url = http_request.get_url()
        query = http_request.get_query()
        headers = http_request.get_headers()
        body = http_request.get_body()
        curl_request = [f'curl -X {method}']
        if body:
            curl_request.append('-d ' + body)
        elif query:
            curl_request.append('-G -d ' + query)
        curl_request.append('-H ' + ' -H '.join(headers))
        curl_request.append(url)
        curl_requests.append(' '.join(curl_request))
    return curl_requests


def send_curl_requests(curl_requests):
    for curl_request in curl_requests:
        system(curl_request)
