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
