general_headings1 = (
    'User-Agent: Mozilla/5.0 (compatible; '
    + 'Konqueror/3.5; Linux) KHTML/3.5.8 (like Gecko)',
    'Pragma: no-cache',
    'Cache-control: no-cache',
)
general_headings2 = (
    'Accept-Encoding: x-gzip, x-deflate, gzip, deflate',
    'Accept-Charset: utf-8, utf-8;q=0.5, *;q=0.5',
    'Accept-Language: en'
)
general_post_put_headings = (
    'Content-Type: application/x-www-form-urlencoded',
    'Connection: close'
)
http_requests = (
    {
        'method': ['GET'],
        'url': ['http://localhost:8080/tienda1/publico/caracteristicas.jsp'],
        'query': ['idA=2'],
        'headers': [
            *general_headings1,
            'Accept: text/xml,application/xml,application/xhtml+xml,'
            + 'text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
            *general_headings2,
            'Host: localhost:8080',
            'Cookie: JSESSIONID=7FD36920003C837664CF0EF535DC10B9',
            'Connection: close'
        ],
        'body': []
    },
    {
        'method': ['POST'],
        'url': ['http://localhost:8080/tienda1/publico/caracteristicas.jsp'],
        'query': [],
        'headers': [
            *general_headings1,
            'Accept: text/xml,application/xml,application/xhtml+xml,'
            + 'text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
            *general_headings2,
            'Host: localhost:8080',
            'Cookie: JSESSIONID=60C9AB659F50A63D09E06E962FC5ABB1',
            *general_post_put_headings,
            'Content-Length: 5'
        ],
        'body': [
            'idA=2'
        ]
    },
    {
        'method': ['PUT'],
        'url': ['http://localhost:8080/tienda1/publico/autenticar.jsp'],
        'query': [],
        'headers': [
            *general_headings1,
            'Accept:text/xml,application/xml,application/xhtml+xml,text/html;'
            + 'q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
            *general_headings2,
            'Host: localhost:9090',
            'Cookie: JSESSIONID=50E143DACA21CB0B6409C4685683A385',
            *general_post_put_headings,
            'Content-Length: 63'
        ],
        'body': [
            'modo=entrar&login=modestin&pwd=c69p04e13&remember'
            + '=off&B1=Entrar'
        ]
    }
)
