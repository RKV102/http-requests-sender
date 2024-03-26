import re


class HttpRequest:
    def __init__(self, string):
        self.method = re.findall(
            pattern=r'^(POST|GET|PUT)(?= )',
            string=string,
            flags=re.M
        )
        self.url = re.findall(
            pattern=(r'(?<=GET ).*?(?=\?| )|(?<=POST ).*?(?= )'
                     r'|(?<=PUT ).*?(?= )'),
            string=string
        )
        self.query = re.findall(pattern=r'(?<=\?).*?(?= HTTP)', string=string)
        self.headers = [
            *re.findall(
                pattern=r'^[A-Z][^A-Z].*?:.*?(?=\n)',
                string=string,
                flags=re.M
            )
        ]
        self.body = re.findall(pattern=r'(?<=\n\n)[^ ]+?(?=\n)', string=string)

    def get_method(self):
        return self.method[0]

    def get_url(self):
        return self.url[0]

    def get_query(self):
        return self.query[0] if self.query else None

    def get_headers(self):
        return self.headers

    def get_body(self):
        return self.body[0] if self.body else None


def get_http_requests(contents):
    return (
        HttpRequest(file_request) for file_requests in (
            re.findall(
                pattern=(r'POST.+?\n\n.+?\n|PUT.+?\n\n.+?\n'
                         r'|GET.+?\n(?=\n)'),
                string=content,
                flags=re.S
            )
            for content in contents
        ) for file_request in file_requests
    )
