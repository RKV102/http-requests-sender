import re


class HttpRequest:
    def __init__(self, string):
        self.method = re.findall(
            pattern='^(POST|GET|PUT)(?= )',
            string=string,
            flags=re.M
        )[0]
        self.url = re.findall(
            pattern=r'(?<=GET ).*?(?=\?| )|(?<=POST ).*?(?= )'
                    + r'|(?<=PUT ).*?(?= )',
            string=string
        )[0]
        self.query = transform(
            re.findall(pattern=r'(?<=\?).*?(?= HTTP)', string=string)
        )
        self.headers = [f'"{item}"' for item in re.findall(
            pattern='^[A-Z][^A-Z].*?:.*?(?=\n)',
            string=string,
            flags=re.M
        )]
        self.body = transform(
            re.findall(pattern='(?<=\n\n)[^ ]+?(?=\n)', string=string)
        )


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
        curl_request = [f'curl -X {http_request.method}']
        if http_request.body:
            curl_request.append('-d ' + http_request.body)
        elif http_request.query:
            curl_request.append('-G -d ' + http_request.query)
        curl_request.append('-H ' + ' -H '.join(http_request.headers))
        curl_request.append(http_request.url)
        curl_requests.append(' '.join(curl_request))
    return curl_requests


def transform(input):
    return f'"{input[0]}"' if input else None
