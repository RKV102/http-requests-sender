def build_curl_requests(http_requests, destination_ip):
    curl_requests = []
    for http_request in http_requests:
        method = http_request.get_method()
        url = http_request.get_url().replace('localhost', destination_ip)
        query = http_request.get_query()
        headers = [
            header if 'localhost' not in header
            else header.replace('localhost', destination_ip)
            for header in http_request.get_headers()
        ]
        body = http_request.get_body()
        curl_request = ['curl', '-X', method]
        if body:
            curl_request = [*curl_request, '-d', body]
        elif query:
            curl_request = [*curl_request, '-G', '-d', query]
        curl_request = [*curl_request, *[
            j for i in [('-H', header) for header in headers] for j in i
        ], url]
        curl_requests.append(curl_request)
    return curl_requests


def send_curl_requests(curl_requests, sender, stdout, stderr):
    for curl_request in curl_requests:
        sender(args=curl_request, stdout=stdout, stderr=stderr)
