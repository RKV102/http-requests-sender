import re


class HttpRequest:
    def __init__(self, string):
        self.method = re.findall(
            pattern='^(POST|GET|PUT)(?= )',
            string=string,
            flags=re.M
        )
        self.url = re.findall(
            pattern=r'(?<=GET ).*?(?=\?| )|(?<=POST ).*?(?= )'
                    + r'|(?<=PUT ).*?(?= )',
            string=string
        )
        self.query = re.findall(pattern=r'(?<=\?).*?(?= HTTP)', string=string)
        self.headers = re.findall(
            pattern='^[A-Z][^A-Z].*?:.*?(?=\n)',
            string=string,
            flags=re.M
        )
        self.body = re.findall(pattern='(?<=\n\n)[^ ]+?(?=\n)', string=string)

    def get_method(self):
        return self.method[0]

    def get_url(self):
        return self.url[0]

    def get_query(self):
        return f'"{self.query[0]}"' if self.query else None

    def get_headers(self):
        return [f'"{header}"' for header in self.headers]

    def get_body(self):
        return f'"{self.body[0]}"' if self.body else None


def get_http_requests(contents):
    return [HttpRequest(j) for i in [
        re.findall(
            pattern='(POST.+?\n\n.+?\n|PUT.+?\n\n.+?\n|GET.+?\n(?=\n))',
            string=content,
            flags=re.S
        )
        for content in contents
    ] for j in i]


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
